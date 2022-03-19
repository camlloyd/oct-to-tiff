import argparse
from pathlib import Path

import numpy as np
import tifffile
from numpy import single, uint16


def main():
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
    parser.add_argument(
        "--angio",
        default=False,
        action="store_true",
        help="convert extracted OCTA data",
    )
    parser.add_argument(
        "--en-face",
        default=False,
        action="store_true",
        help="convert extracted en face image",
    )
    parser.add_argument(
        "--seg-curve",
        default=False,
        action="store_true",
        help="convert extracted segmentation data",
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.2.0")
    args = parser.parse_args()

    file_path = args.input
    file_name = file_path.stem
    if args.output:
        dir_name = args.output
        dir_name.mkdir(parents=True, exist_ok=True)
    else:
        dir_name = file_path.parent
    output_path = dir_name / (file_name + ".ome.tif")

    def convert_oct_file():
        with open(file_path, "rb") as f:
            if "3D Cornea" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 106
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 513
                pixel_size_x = 0.007797
                pixel_size_y = 0.003071
                pixel_size_z = 0.040000
            elif "3D Disc" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 106
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 513
                pixel_size_x = 0.011696
                pixel_size_y = 0.003071
                pixel_size_z = 0.060000
            elif "3D Retina" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 144
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 385
                pixel_size_x = 0.018182
                pixel_size_y = 0.003071
                pixel_size_z = 0.050000
            elif "3D Widefield MCT" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 320
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 320
                pixel_size_x = 0.003075
                pixel_size_y = 0.003071
                pixel_size_z = 0.028125
            elif "3D Widefield" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 323
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 320
                pixel_size_x = 0.003075
                pixel_size_y = 0.003071
                pixel_size_z = 0.028125
            elif "Angle" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 768
                xy_scan_length = 1020
                pixel_size_x = 0.002941
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Cornea Cross Line" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 2
                total_data_groups = 2
                oct_window_height = 640
                xy_scan_length = 941
                pixel_size_x = 0.008502
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Cornea Line" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 640
                xy_scan_length = 1020
                pixel_size_x = 0.007843
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Cross Line" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 2
                total_data_groups = 2
                oct_window_height = 768
                xy_scan_length = 1020
                pixel_size_x = 0.009804
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Enhanced HD Line" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 960
                xy_scan_length = 998
                pixel_size_x = 0.012024
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "GCC" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 16
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 933
                pixel_size_x = 0.007503
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Grid" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 10
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1020
                pixel_size_x = 0.005882
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "HD Angio Disc" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
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
                volume = np.frombuffer(f.read(), dtype=single)
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
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 400
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 400
                pixel_size_x = 0.015000
                pixel_size_y = 0.003071
                pixel_size_z = 0.015000
            elif "Angio Retina" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
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
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 18
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1024
                pixel_size_x = 0.009766
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Line" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 960
                xy_scan_length = 1020
                pixel_size_x = 0.008824
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "PachymetryWide" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 16
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1536
                pixel_size_x = 0.005859
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif "Raster" in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 21
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 1020
                pixel_size_x = 0.011765
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif args.angio and args.size:
                volume = np.frombuffer(f.read(), dtype=uint16)
                oct_window_height = 160
                frames_per_data_group = int((len(volume) // oct_window_height) ** 0.5)
                total_data_groups = 1
                xy_scan_length = int((len(volume) // oct_window_height) ** 0.5)
                pixel_size_x = args.size / xy_scan_length
                pixel_size_y = 0.012283
                pixel_size_z = args.size / frames_per_data_group
            elif args.en_face and args.size:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 1
                oct_window_height = int(len(volume) ** 0.5)
                xy_scan_length = int(len(volume) ** 0.5)
                pixel_size_x = args.size / oct_window_height
                pixel_size_y = args.size / xy_scan_length
                pixel_size_z = 1
            elif args.seg_curve:
                volume = np.frombuffer(f.read(), dtype=single)
                if len(volume) == 1280000 or len(volume) == 1120000:
                    frames_per_data_group = 400
                    oct_window_height = 400
                elif len(volume) == 739328 or len(volume) == 646912:
                    frames_per_data_group = 304
                    oct_window_height = 304
                total_data_groups = 1
                xy_scan_length = len(volume) // (
                    frames_per_data_group * oct_window_height
                )
                pixel_size_x = 1
                pixel_size_y = 1
                pixel_size_z = 1

            # Reshape array into 3 dimensions.
            volume = np.reshape(
                volume,
                (
                    frames_per_data_group * total_data_groups,
                    xy_scan_length,
                    oct_window_height,
                ),
            )

            # Rotate array 90 degrees left (anti-clockwise) about the z-axis.
            if not args.en_face and not args.seg_curve:
                volume = np.rot90(volume, k=1, axes=(1, 2))

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

    if Path.is_file(output_path):
        if args.overwrite:
            convert_oct_file()
        else:
            print(str(output_path) + " already exists.")
    else:
        convert_oct_file()


if __name__ == "__main__":
    main()
