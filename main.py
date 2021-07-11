import argparse
import numpy as np
import tifffile as tifffile
from numpy import single
from pathlib import Path

parser = argparse.ArgumentParser(description='Convert optical coherence tomography (.OCT) files to TIFF.')
parser.add_argument('input', type=str, help='.OCT file to convert')
args = parser.parse_args()

file_path = args.input
file_name = Path(file_path).stem
with open(file_path, 'rb') as f:
    volume = np.frombuffer(f.read(), dtype=single)
    if '3D Cornea' in file_name:
        frames_per_data_group = 106
        total_data_groups = 1
        oct_window_height = 640
        xy_scan_length = 513
        pixel_size_x = 0.007797
        pixel_size_y = 0.003071
        pixel_size_z = 1
    elif 'Cornea Cross Line' in file_name:
        frames_per_data_group = 2
        total_data_groups = 2
        oct_window_height = 640
        xy_scan_length = 941
        pixel_size_x = 0.008502
        pixel_size_y = 0.003071
        pixel_size_z = 1
    elif 'HD Angio Retina' in file_name:
        frames_per_data_group = 400
        total_data_groups = 1
        oct_window_height = 640
        xy_scan_length = 400
        pixel_size_x = 0.015000
        pixel_size_y = 0.003071
        pixel_size_z = 0.015000
    elif 'PachymetryWide' in file_name:
        frames_per_data_group = 16
        total_data_groups = 1
        oct_window_height = 640
        xy_scan_length = 1536
        pixel_size_x = 0.005859
        pixel_size_y = 0.003071
        pixel_size_z = 1

    # Reshape array into 3 dimensions.
    volume = np.reshape(volume, (frames_per_data_group * total_data_groups, xy_scan_length, oct_window_height))

    # Rotate array 90 degrees left (anti-clockwise) about the z-axis.
    volume = np.rot90(volume, k=1, axes=(1, 2))

    dir_name = Path(file_path).parent
    tifffile.imwrite(dir_name / (file_name + '.tif'), volume, imagej=True, photometric='minisblack', resolution=(1. / pixel_size_x, 1. / pixel_size_y), metadata={'spacing': pixel_size_z, 'unit': 'mm', 'axes': 'ZYX'})
