import argparse
import logging
from importlib.metadata import version
from pathlib import Path
from typing import Any

import defusedxml.ElementTree as DET
import numpy as np
import tifffile
from numpy.typing import NDArray

logger = logging.getLogger(__name__)


def reshape_volume(
    volume: NDArray[Any],
    frames_per_data_group: int,
    total_data_groups: int,
    oct_window_height: int,
    xy_scan_length: int,
) -> NDArray[Any]:
    """Reshape a 1-dimensional array to a 3-dimensional array.

    Parameters
    ----------
    volume : NDArray[Any]
        A 1-dimensional array.
    frames_per_data_group : int
        The number of frames per data group.
    total_data_groups : int
        The total number of data groups.
    oct_window_height : int
        The OCT window height.
    xy_scan_length : int
        The XY scan length.

    Returns
    -------
    volume : NDArray[Any]
        A 3-dimensional array.

    """
    volume = np.reshape(
        volume,
        (
            frames_per_data_group * total_data_groups,
            xy_scan_length,
            oct_window_height,
        ),
    )
    return volume


def write_volume(
    output_path: Path,
    volume: NDArray[Any],
    pixel_size_x: float,
    pixel_size_y: float,
    pixel_size_z: float,
) -> None:
    """Write a 3-dimensional array to the output path as an OME-TIFF file, including voxel size in the metadata.

    Parameters
    ----------
    output_path : Path
        The specified output path.
    volume : NDArray[Any]
        A 3-dimensional array.
    pixel_size_x : float
        The pixel (voxel) width in mm.
    pixel_size_y : float
        The pixel (voxel) height in mm.
    pixel_size_z : float
        The pixel (voxel) depth in mm.

    """
    tifffile.imwrite(
        output_path,
        volume,
        photometric="minisblack",
        metadata={
            "axes": "ZYX",
            "PhysicalSizeX": pixel_size_x,
            "PhysicalSizeXUnit": "mm",
            "PhysicalSizeY": pixel_size_y,
            "PhysicalSizeYUnit": "mm",
            "PhysicalSizeZ": pixel_size_z,
            "PhysicalSizeZUnit": "mm",
        },
    )


def extract_boundaries(input_path: str | Path) -> None:
    """Extract segmentation lines.

    Parameters
    ----------
    input_path : str | Path
        The specified input path.

    """
    input_path = Path(input_path)
    tree = DET.parse(input_path)
    root = tree.getroot()

    array_size = int(root.findtext("./Curve_Set/Image/Curve/ARRAY", 0))
    data_points = [
        int(point.text) if point.text else 0
        for point in root.findall("./Curve_Set/Image/Curve/D")
    ]
    scan_length = np.arange(len(data_points))
    num_files = len(data_points) // array_size
    for i in range(num_files):
        start = i * array_size
        end = start + array_size
        table = np.column_stack([scan_length[start:end], data_points[start:end]])
        table_path = f"{input_path.parent}/{input_path.stem}_{i+1}.txt"
        np.savetxt(table_path, table, delimiter="\t", fmt="%d")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert optical coherence tomography angiography (OCTA) data."
    )
    parser.add_argument("input", type=Path, help="OCT file to convert")
    parser.add_argument("--output", type=Path, help="specify a custom output directory")
    parser.add_argument(
        "--overwrite",
        default=False,
        action="store_true",
        help="overwrite output file if it exists",
    )
    parser.add_argument("--size", type=float, help="scan size in mm")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--angio",
        default=False,
        action="store_true",
        help="convert extracted OCTA data",
    )
    group.add_argument(
        "--en-face",
        default=False,
        action="store_true",
        help="convert extracted en face image",
    )
    group.add_argument(
        "--seg-curve",
        default=False,
        action="store_true",
        help="convert extracted segmentation data",
    )
    group.add_argument(
        "--boundaries",
        default=False,
        action="store_true",
        help="extract segmentation lines",
    )
    parser.add_argument(
        "--log-level",
        default="WARNING",
        metavar="LEVEL",
        help="sets the logging level (default: %(default)s)",
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + version("oct_to_tiff")
    )
    args = parser.parse_args()

    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {args.log_level}")
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s %(name)s:%(funcName)s %(levelname)s - %(message)s",
    )

    input_path = args.input
    if args.output:
        dir_name = args.output
        dir_name.mkdir(parents=True, exist_ok=True)
    else:
        dir_name = input_path.parent
    file_name = input_path.stem
    file_extension = ".ome.tif"
    output_path = dir_name / (file_name + file_extension)

    if Path.is_file(output_path):
        if args.overwrite:
            logger.warning(f"Overwriting {output_path}")
        else:
            logger.error(f"{output_path} already exists.")
            return

    if args.boundaries:
        extract_boundaries(input_path)
        return

    with open(input_path, "rb") as f:
        if args.angio and args.size:
            volume = np.frombuffer(f.read(), dtype=np.uint16)
            oct_window_height = 160
            frames_per_data_group = int((len(volume) // oct_window_height) ** 0.5)
            total_data_groups = 1
            xy_scan_length = int((len(volume) // oct_window_height) ** 0.5)
            pixel_size_x = args.size / xy_scan_length
            pixel_size_y = 0.012283
            pixel_size_z = args.size / frames_per_data_group
        elif args.en_face and args.size:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 1
            total_data_groups = 1
            oct_window_height = int(len(volume) ** 0.5)
            xy_scan_length = int(len(volume) ** 0.5)
            pixel_size_x = args.size / oct_window_height
            pixel_size_y = args.size / xy_scan_length
            pixel_size_z = 1
        elif args.seg_curve:
            volume = np.frombuffer(f.read(), dtype=np.single)
            if len(volume) == 1280000 or len(volume) == 1120000:
                frames_per_data_group = 400
                oct_window_height = 400
            elif len(volume) == 739328 or len(volume) == 646912:
                frames_per_data_group = 304
                oct_window_height = 304
            total_data_groups = 1
            xy_scan_length = len(volume) // (frames_per_data_group * oct_window_height)
            pixel_size_x = 1
            pixel_size_y = 1
            pixel_size_z = 1
        elif "3D Cornea" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 106
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 513
            pixel_size_x = 0.007797
            pixel_size_y = 0.003071
            pixel_size_z = 0.040000
        elif "3D Disc" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 106
            total_data_groups = 1
            oct_window_height = 768
            xy_scan_length = 513
            pixel_size_x = 0.011696
            pixel_size_y = 0.003071
            pixel_size_z = 0.060000
        elif "3D Retina" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 144
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 385
            pixel_size_x = 0.018182
            pixel_size_y = 0.003071
            pixel_size_z = 0.050000
        elif "3D Widefield MCT" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 320
            total_data_groups = 1
            oct_window_height = 768
            xy_scan_length = 320
            pixel_size_x = 0.003075
            pixel_size_y = 0.003071
            pixel_size_z = 0.028125
        elif "3D Widefield" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 323
            total_data_groups = 1
            oct_window_height = 768
            xy_scan_length = 320
            pixel_size_x = 0.003075
            pixel_size_y = 0.003071
            pixel_size_z = 0.028125
        elif "Angle" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 1
            total_data_groups = 2
            oct_window_height = 768
            xy_scan_length = 1020
            pixel_size_x = 0.002941
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Cornea Cross Line" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 2
            total_data_groups = 2
            oct_window_height = 640
            xy_scan_length = 941
            pixel_size_x = 0.008502
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Cornea Line" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 1
            total_data_groups = 2
            oct_window_height = 640
            xy_scan_length = 1020
            pixel_size_x = 0.007843
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Cross Line" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 2
            total_data_groups = 2
            oct_window_height = 768
            xy_scan_length = 1020
            pixel_size_x = 0.009804
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Enhanced HD Line" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 1
            total_data_groups = 2
            oct_window_height = 960
            xy_scan_length = 998
            pixel_size_x = 0.012024
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "GCC" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 16
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 933
            pixel_size_x = 0.007503
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Grid" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 10
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 1020
            pixel_size_x = 0.005882
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "HD Angio Disc" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 400
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 400
            pixel_size_x = 0.011250
            pixel_size_y = 0.003071
            pixel_size_z = 0.011250
            if args.size:
                pixel_size_x = args.size / xy_scan_length
                pixel_size_z = args.size / frames_per_data_group
        elif "Angio Disc" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 304
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 304
            pixel_size_x = 0.009868
            pixel_size_y = 0.003071
            pixel_size_z = 0.009868
            if args.size:
                pixel_size_x = args.size / xy_scan_length
                pixel_size_z = args.size / frames_per_data_group
        elif "HD Angio Retina" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 400
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 400
            pixel_size_x = 0.015000
            pixel_size_y = 0.003071
            pixel_size_z = 0.015000
        elif "Angio Retina" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 304
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 304
            pixel_size_x = 0.019737
            pixel_size_y = 0.003071
            pixel_size_z = 0.019737
            if args.size:
                pixel_size_x = args.size / xy_scan_length
                pixel_size_z = args.size / frames_per_data_group
        elif "Radial Lines" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 18
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 1024
            pixel_size_x = 0.009766
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Line" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 1
            total_data_groups = 2
            oct_window_height = 960
            xy_scan_length = 1020
            pixel_size_x = 0.008824
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "ONH" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single, count=2223360)
            frames_per_data_group = 3
            total_data_groups = 1
            oct_window_height = 768
            xy_scan_length = 965
            pixel_size_x = 0.015952
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "PachymetryWide" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 16
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 1536
            pixel_size_x = 0.005859
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Raster" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single)
            frames_per_data_group = 21
            total_data_groups = 1
            oct_window_height = 768
            xy_scan_length = 1020
            pixel_size_x = 0.011765
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif "Retina Map" in file_name:
            volume = np.frombuffer(f.read(), dtype=np.single, count=6680960)
            frames_per_data_group = 13
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 803
            pixel_size_x = 0.007472
            pixel_size_y = 0.003071
            pixel_size_z = 1

        volume = reshape_volume(
            volume,
            frames_per_data_group,
            total_data_groups,
            oct_window_height,
            xy_scan_length,
        )

        if not args.en_face and not args.seg_curve:
            volume = np.rot90(volume, k=1, axes=(1, 2))

        write_volume(output_path, volume, pixel_size_x, pixel_size_y, pixel_size_z)


if __name__ == "__main__":
    main()
