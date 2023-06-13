# oct-to-tiff

[![DOI](https://zenodo.org/badge/382486199.svg)](https://zenodo.org/badge/latestdoi/382486199)

A command line tool for converting optical coherence tomography angiography (OCTA) data.

## Installation
via pip:

    pip install oct-to-tiff

via conda:

    conda install -c conda-forge oct-to-tiff

## Getting started
    oct-to-tiff /path/to/image.OCT
    
will read an OCT volume and write to a single OME-TIFF file, including voxel size in the metadata.

By default, the output file will be written with the same name as the input file and to the same directory:


    tree /path/to/images
        ├── image.OCT
        └── image.ome.tif

To specify a custom output directory, see [Optional arguments](#optional-arguments) below.

## Supported scan patterns

This tool has been developed by reverse engineering data from the Optovue RTVue XR Avanti System.

Due to limited test data, only the following scan patterns are currently supported:

### Structural OCT
- 3D Cornea
- 3D Disc
- 3D Retina
- 3D Widefield
- 3D Widefield MCT
- Angle
- Cornea Cross Line
- Cornea Line
- Cross Line
- Enhanced HD Line
- GCC
- Grid
- Line
- ONH (Partial)
- Pachymetry Wide
- Radial Lines
- Raster
- Retina Map (Partial)

### OCT Angiography
- Angio Disc
- Angio Retina
- HD Angio Disc
- HD Angio Retina


## Optional arguments

To view these options at any time, run `oct-to-tiff --help`.

#### `--output OUTPUT`
**Description**: specify a custom output directory. 

If the path to the output directory does not exist, a new directory (and parent directories) will be created.

**Usage**: 
    
    oct-to-tiff /path/to/image.OCT --output /path/to/output/directory
    
#### `--overwrite`
**Description**: overwrite output file if it exists.

**Usage**: 
    
    oct-to-tiff /path/to/image.OCT --overwrite
    
#### `--size SIZE`
**Description**: scan size in mm.

Sets the correct voxel size for scan patterns with adjustable length.

**Usage**:

    oct-to-tiff /path/to/image.OCT --size 4.5

#### `--version`
**Description**: show program's version number and exit.

**Usage**:

    oct-to-tiff --version

#### The following options are mutually exclusive:
    
#### `--angio`
**Description**: convert extracted OCTA data. 

Requires `--size SIZE`.

**Usage**:

    oct-to-tiff /path/to/data --angio --size 4.5
    
#### `--en-face`
**Description**: convert extracted en face data.

Requires `--size SIZE`.

**Usage**:

    oct-to-tiff /path/to/data --en-face --size 4.5
    
#### `--seg-curve`
**Description**: convert extracted segmentation data.

**Usage**:

    oct-to-tiff /path/to/data --seg-curve

#### `--boundaries`
**Description**: extract segmentation lines.

**Usage**:

    oct-to-tiff /path/to/curve.xml --boundaries

## Contributing

This project uses [black](https://github.com/psf/black) for formatting and [isort](https://github.com/PyCQA/isort) for sorting imports.

## Requirements

Requires Python 3.8 or higher.