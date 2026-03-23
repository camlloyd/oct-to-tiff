from pathlib import Path

import numpy as np
from roifile import ROI_TYPE, roiread

from oct_to_tiff.cli import (
    arrays_to_rois,
    boundaries_to_arrays,
    reshape_volume,
    volume_metadata,
)


def test_arrays_to_rois_returns_freeline_rois_from_arrays(tmp_path: Path) -> None:
    # Arrange
    arrays = [
        np.array([[0, 101], [1, 102], [2, 103]]),
        np.array([[0, 99], [1, 98], [2, 97]]),
    ]
    output_path = tmp_path / "rois.zip"

    # Act
    arrays_to_rois(arrays, output_path)

    # Assert
    result = roiread(output_path)
    assert len(result) == 2
    for roi in result:
        assert roi.roitype == ROI_TYPE.FREELINE


def test_boundaries_to_arrays_returns_arrays_from_curve_xml(tmp_path: Path) -> None:
    # Arrange
    valid_curve_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <Curve>
            <Curve_Set>
                <Image>
                    <Curve>
                        <ARRAY>3</ARRAY>
                        <D>101</D>
                        <D>102</D>
                        <D>103</D>
                    </Curve>
                    <Curve>
                        <ARRAY>3</ARRAY>
                        <D>99</D>
                        <D>98</D>
                        <D>97</D>
                    </Curve>
                </Image>
            </Curve_Set>
        </Curve>
    """
    input_path = tmp_path / "curve.xml"
    input_path.write_text(valid_curve_xml)

    # Act
    result = boundaries_to_arrays(input_path)

    # Assert
    expected = [
        np.array([[0, 101], [1, 102], [2, 103]]),
        np.array([[0, 99], [1, 98], [2, 97]]),
    ]
    np.testing.assert_array_equal(result, expected)


def test_reshape_volume_returns_3d_array_from_1d_array() -> None:
    # Arrange
    volume = np.arange(8, dtype=np.float32)

    # Act
    result = reshape_volume(
        volume,
        frames_per_data_group=2,
        total_data_groups=1,
        oct_window_height=2,
        xy_scan_length=2,
    )

    # Assert
    expected = np.array(
        [
            [[0, 1], [2, 3]],
            [[4, 5], [6, 7]],
        ],
        dtype=np.float32,
    )
    np.testing.assert_array_equal(result, expected)


def test_volume_metadata_returns_axes_only_when_pixel_sizes_are_none() -> None:
    # Arrange
    pixel_size_x = None
    pixel_size_y = None
    pixel_size_z = None

    # Act
    result = volume_metadata(pixel_size_x, pixel_size_y, pixel_size_z)

    # Assert
    expected = {"axes": "ZYX"}
    assert result == expected


def test_volume_metadata_returns_physical_sizes_and_units() -> None:
    # Arrange
    pixel_size_x = 0.01
    pixel_size_y = 0.02
    pixel_size_z = 0.03

    # Act
    result = volume_metadata(pixel_size_x, pixel_size_y, pixel_size_z)

    # Assert
    expected = {
        "axes": "ZYX",
        "PhysicalSizeX": 0.01,
        "PhysicalSizeY": 0.02,
        "PhysicalSizeZ": 0.03,
        "PhysicalSizeXUnit": "mm",
        "PhysicalSizeYUnit": "mm",
        "PhysicalSizeZUnit": "mm",
    }
    assert result == expected
