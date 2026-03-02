# CHANGELOG

<!-- version list -->

## v0.6.2 (2026-03-02)

### Bug Fixes

- **cli**: Raise error if scan pattern not found
  ([`d8bc512`](https://github.com/camlloyd/oct-to-tiff/commit/d8bc5126e0b45b7da3d1caabf239b0b3f6de7632))

### Code Style

- **cli**: Format docstrings
  ([`f5cad41`](https://github.com/camlloyd/oct-to-tiff/commit/f5cad41fc04e1536404be4c391593b9fb70197af))

### Documentation

- **citation**: Update CITATION.cff
  ([`916d5bd`](https://github.com/camlloyd/oct-to-tiff/commit/916d5bd936b8c6c7eebad9c1292aadb5d5d77e8a))

- **cli**: Update `write_volume` docstring
  ([`63ab2a1`](https://github.com/camlloyd/oct-to-tiff/commit/63ab2a1546aa04b5c7f6d23cc009ee6778d06a90))


## v0.6.1 (2026-02-03)

### Bug Fixes

- **cli**: Allow pixel size to be `None`
  ([`98030b9`](https://github.com/camlloyd/oct-to-tiff/commit/98030b9442044025e00b669b9f0b80796fcb3079))

### Build System

- Use uv build backend
  ([`dc96917`](https://github.com/camlloyd/oct-to-tiff/commit/dc969173207bffb836a718999e0c057fa26389f2))

- **dockerfile**: Bump python version to 3.11.14
  ([`1faabef`](https://github.com/camlloyd/oct-to-tiff/commit/1faabeff8571b3638a0f2fd82b6076e9b2815348))

- **dockerignore**: Relax excluded files for uv
  ([`f4eb716`](https://github.com/camlloyd/oct-to-tiff/commit/f4eb716b10841f2ce994dcd5c2e4049e6cce55c4))

- **pyproject**: Bump uv build version to 0.9.26
  ([`3f3a1a8`](https://github.com/camlloyd/oct-to-tiff/commit/3f3a1a8e51da5fdf97f8937b24a30dd28acb7849))

### Chores

- **config**: Allow zero version
  ([`9765198`](https://github.com/camlloyd/oct-to-tiff/commit/97651986b83315440543dbe8e6b62d65a41b5fae))

- **config**: Configure Python Semantic Release
  ([`4a28651`](https://github.com/camlloyd/oct-to-tiff/commit/4a286510feec829888cdc05e9d7639523c2e9a0a))

### Documentation

- **readme**: Update installation via conda
  ([`2fd6a88`](https://github.com/camlloyd/oct-to-tiff/commit/2fd6a888a7c910aa58b6736571533b238d6a9f16))

### Refactoring

- **cli**: Separate metadata
  ([`4068d17`](https://github.com/camlloyd/oct-to-tiff/commit/4068d1786587673e9f0073015e4b4e168d8f4623))


## v0.6.0 (2025-10-12)
* Remove `rotate_volume()` helper function
* Warn when using `--overwrite`
* Split 3D Cornea `Main` and `Align` scans
* Add support for ImageJ ROIs
* Drop support for Python 3.10
* Refactoring


## v0.5.0 (2024-12-06)
* Add --log-level optional argument
* Add type hints
* Drop support for Python 3.8 and 3.9
* Update Docker build
* Add workflow for publishing to Docker Hub
* Set missing data points to default value of `0`


## v0.4.0 (2023-07-18)
* Add support for extracting segmentation lines
* Add mutually exclusive group to parser
* Drop support for Python 3.7
* Refactoring


## v0.3.0 (2022-11-13)
* Add support for Retina Map scan pattern
* Add support for ONH scan pattern
* Add basic logging functionality
* Add workflow for publishing to PyPI
* Add CITATION.cff
* Update GitHub action versions
* Refactoring


## v0.2.0 (2022-03-19)
* Add support for en face images
* Add support for segmentation data
* Add --output optional argument for specifying a custom output directory
* Add workflow for publishing to TestPyPI
* Fix --size optional argument description
* Format using black and sort imports using isort
* Prepare for Zenodo release
* Refactoring


## v0.1.1 (2021-12-30)
* Fixed bug when checking for 3D Disc scan pattern


## v0.1.0 (2021-11-07)
* Initial release
