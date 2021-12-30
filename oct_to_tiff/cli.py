import argparse
import numpy as np
import tifffile
from numpy import single, uint16
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Convert optical coherence tomography angiography (OCTA) data.')
    parser.add_argument('input', type=str, help='OCT file to convert')
    parser.add_argument('--overwrite', default=False, action='store_true', help='overwrite output file if it exists')
    parser.add_argument('--size', type=float, help='scan size in mm^2')
    parser.add_argument('--angio', default=False, action='store_true', help='convert extracted OCTA data')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1.1')
    args = parser.parse_args()

    file_path = args.input
    file_name = Path(file_path).stem
    dir_name = Path(file_path).parent
    output_path = dir_name / (file_name + '.ome.tif')

    def convert_oct_file():
        with open(file_path, 'rb') as f:
            if '3D Cornea' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 106
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 513
                pixel_size_x = 0.007797
                pixel_size_y = 0.003071
                pixel_size_z = 0.040000
            elif '3D Disc' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 106
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 513
                pixel_size_x = 0.011696
                pixel_size_y = 0.003071
                pixel_size_z = 0.060000
            elif '3D Retina' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 144
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 385
                pixel_size_x = 0.018182
                pixel_size_y = 0.003071
                pixel_size_z = 0.050000
            elif '3D Widefield MCT' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 320
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 320
                pixel_size_x = 0.003075
                pixel_size_y = 0.003071
                pixel_size_z = 0.028125
            elif '3D Widefield' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 323
                total_data_groups = 1
                oct_window_height = 768
                xy_scan_length = 320
                pixel_size_x = 0.003075
                pixel_size_y = 0.003071
                pixel_size_z = 0.028125
            elif 'Angle' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 768
                xy_scan_length = 1020
                pixel_size_x = 0.002941
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Cornea Cross Line' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 2
                total_data_groups = 2
                oct_window_height = 640
                xy_scan_length = 941
                pixel_size_x = 0.008502
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Cornea Line' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 640
                xy_scan_length = 1020
                pixel_size_x = 0.007843
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Cross Line' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 2
                total_data_groups = 2
                oct_window_height = 768
                xy_scan_length = 1020
                pixel_size_x = 0.009804
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Enhanced HD Line' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 960
                xy_scan_length = 998
                pixel_size_x = 0.012024
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'GCC' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 16
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 933
                pixel_size_x = 0.007503
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Grid' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 10
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1020
                pixel_size_x = 0.005882
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'HD Angio Disc' in file_name:
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
            elif 'Angio Disc' in file_name:
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
            elif 'HD Angio Retina' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 400
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 400
                pixel_size_x = 0.015000
                pixel_size_y = 0.003071
                pixel_size_z = 0.015000
            elif 'Angio Retina' in file_name:
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
            elif 'Radial Lines' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 18
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1024
                pixel_size_x = 0.009766
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Line' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 1
                total_data_groups = 2
                oct_window_height = 960
                xy_scan_length = 1020
                pixel_size_x = 0.008824
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'PachymetryWide' in file_name:
                volume = np.frombuffer(f.read(), dtype=single)
                frames_per_data_group = 16
                total_data_groups = 1
                oct_window_height = 640
                xy_scan_length = 1536
                pixel_size_x = 0.005859
                pixel_size_y = 0.003071
                pixel_size_z = 1
            elif 'Raster' in file_name:
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
                if len(volume) == 25600000:
                    frames_per_data_group = 400
                    xy_scan_length = 400
                elif len(volume) == 14786560:
                    frames_per_data_group = 304
                    xy_scan_length = 304
                total_data_groups = 1
                oct_window_height = 160
                pixel_size_x = args.size / xy_scan_length
                pixel_size_y = 0.012283
                pixel_size_z = args.size / frames_per_data_group

            # Reshape array into 3 dimensions.
            volume = np.reshape(volume, (frames_per_data_group * total_data_groups, xy_scan_length, oct_window_height))

            # Rotate array 90 degrees left (anti-clockwise) about the z-axis.
            volume = np.rot90(volume, k=1, axes=(1, 2))

            tifffile.imwrite(output_path, volume, photometric='minisblack',
                             metadata={'axes': 'ZYX', 'PhysicalSizeX': pixel_size_x, 'PhysicalSizeXUnit': 'mm',
                                       'PhysicalSizeY': pixel_size_y, 'PhysicalSizeYUnit': 'mm',
                                       'PhysicalSizeZ': pixel_size_z,
                                       'PhysicalSizeZUnit': 'mm'})

    if Path.is_file(output_path):
        if args.overwrite:
            convert_oct_file()
        else:
            print(str(output_path) + " already exists.")
    else:
        convert_oct_file()


if __name__ == '__main__':
    main()
