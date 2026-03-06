from pathlib import Path

import numpy as np

from oct_to_tiff.cli import boundaries_to_arrays


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
