import argparse
import numpy as np
import tifffile as tifffile
from numpy import single, uint16
from pathlib import Path

parser = argparse.ArgumentParser(description='Convert optical coherence tomography (.OCT) files to TIFF.')
parser.add_argument('input', type=str, help='.OCT file to convert')
parser.add_argument('--overwrite', default=False, action='store_true', help='overwrite output file if it exists')
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
        elif 'Cornea Cross Line' in file_name:
            volume = np.frombuffer(f.read(), dtype=single)
            frames_per_data_group = 2
            total_data_groups = 2
            oct_window_height = 640
            xy_scan_length = 941
            pixel_size_x = 0.008502
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif 'HD Angio Retina' in file_name:
            volume = np.frombuffer(f.read(), dtype=single)
            frames_per_data_group = 400
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 400
            pixel_size_x = 0.015000
            pixel_size_y = 0.003071
            pixel_size_z = 0.015000
        elif 'PachymetryWide' in file_name:
            volume = np.frombuffer(f.read(), dtype=single)
            frames_per_data_group = 16
            total_data_groups = 1
            oct_window_height = 640
            xy_scan_length = 1536
            pixel_size_x = 0.005859
            pixel_size_y = 0.003071
            pixel_size_z = 1
        elif Path(file_name).suffix == '':
            volume = np.frombuffer(f.read(), dtype=uint16)
            if len(volume) == 25600000:
                frames_per_data_group = 400
                total_data_groups = 1
                oct_window_height = 160
                xy_scan_length = 400
                pixel_size_x = 0.015000
                pixel_size_y = 0.012283
                pixel_size_z = 0.015000
            elif len(volume) == 14786560:
                frames_per_data_group = 304
                total_data_groups = 1
                oct_window_height = 160
                xy_scan_length = 304
                pixel_size_x = 0.015000
                pixel_size_y = 0.003071
                pixel_size_z = 0.015000

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
