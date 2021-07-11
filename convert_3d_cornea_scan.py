import numpy as np
import tifffile as tifffile
from numpy import single
from pathlib import Path

file_path = '/path/to/file.OCT'
with open(file_path, 'rb') as f:
    volume = np.frombuffer(f.read(), dtype=single)

    # Reshape array into 3 dimensions.
    frames_per_data_group = 106
    total_data_groups = 1
    oct_window_height = 640
    xy_scan_length = 513
    volume = np.reshape(volume, (frames_per_data_group * total_data_groups, xy_scan_length, oct_window_height))

    # Rotate array 90 degrees left (anti-clockwise) about the z-axis.
    volume = np.rot90(volume, k=1, axes=(1, 2))

    dir_name = Path(file_path).parent
    file_name = Path(file_path).stem
    pixel_size_x = 0.007797
    pixel_size_y = 0.003071
    pixel_size_z = 1
    tifffile.imwrite(dir_name / (file_name + '.tif'), volume, imagej=True, photometric='minisblack', resolution=(1. / pixel_size_x, 1. / pixel_size_y), metadata={'spacing': pixel_size_z, 'unit': 'mm', 'axes': 'ZYX'})
