# oct-to-tiff

A command line tool for converting optical coherence tomography angiography (OCTA) data.

## Installation
    pip install oct-to-tiff

## Getting Started
    oct-to-tiff /path/to/image.OCT
    
will read an OCT volume and write to a single OME-TIFF file, including voxel size in the metadata.

For more options, run `oct-to-tiff --help`.
    
## Supported scan patterns

This tool has been developed for use with data from the Optovue RTVue XR Avanti System.

Due to limited test data, only the following scan patterns are currently supported:

### OCT
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
- Pachymetry Wide
- Radial Lines
- Raster

### OCTA
- Angio Disc
- Angio Retina
- HD Angio Disc
- HD Angio Retina

## Requirements

Requires Python 3.7 or higher.