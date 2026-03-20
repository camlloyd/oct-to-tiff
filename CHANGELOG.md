# CHANGELOG

<!-- version list -->

## v0.6.3 (2026-03-20)

### Bug Fixes

- **cli**: Make `--size` optional
  ([`dd2be67`](https://github.com/camlloyd/oct-to-tiff/commit/dd2be67180aad23c04579bd44f36a58affefd613))

- **cli**: Raise error if xml root not found
  ([`eea3e01`](https://github.com/camlloyd/oct-to-tiff/commit/eea3e0143536d3c70c31f7e19e346965e956ccae))

### Build System

- **docker**: Bump python version to 3.11.15
  ([`5ea83c3`](https://github.com/camlloyd/oct-to-tiff/commit/5ea83c3f49da513e0b187bd8d22da8cde20f80cf))

- **dockerignore**: Ignore caches
  ([`067ef94`](https://github.com/camlloyd/oct-to-tiff/commit/067ef943fd3c7c5db2d8ec8fc38a18597b82a256))

- **dockerignore**: Ignore test artifacts
  ([`6ff2b1d`](https://github.com/camlloyd/oct-to-tiff/commit/6ff2b1dbfc6223ebf13fdc99071b861a9a6ace91))

- **pyproject**: Bump uv build version
  ([`861fb98`](https://github.com/camlloyd/oct-to-tiff/commit/861fb98972ce72b3d83fd25d182af9d27d13d336))

### Chores

- **issues**: Disable blank issues
  ([`432025a`](https://github.com/camlloyd/oct-to-tiff/commit/432025a925ccfef71cbcd5a2ecfc3c4848008ce4))

- **issues**: Migrate bug report template
  ([`fae9c64`](https://github.com/camlloyd/oct-to-tiff/commit/fae9c64dc31ab19dab729e9f21e0908859640b09))

- **issues**: Migrate feature request template
  ([`913e42f`](https://github.com/camlloyd/oct-to-tiff/commit/913e42fc6b982121ed15b30620a79b18188d6b83))

- **pre-commit**: Bump hook versions
  ([`edce3e7`](https://github.com/camlloyd/oct-to-tiff/commit/edce3e7cd0258e9b9f8f08eb52ba0a606f692c86))

- **pre-commit**: Remove quotes from `ruff-check` hook args
  ([`6bf1555`](https://github.com/camlloyd/oct-to-tiff/commit/6bf155501c4bed99965557f130582c3b08c44a20))

- **pre-commit**: Use `ruff-check` hook ID
  ([`5d74a3b`](https://github.com/camlloyd/oct-to-tiff/commit/5d74a3bd7247d663f379411c267f06258fc852aa))

- **pyproject**: Add prek to dev dependencies
  ([`818f770`](https://github.com/camlloyd/oct-to-tiff/commit/818f7701c1851529eb8b8425cfb03ddddb2f287a))

### Continuous Integration

- Bump actions/attest-build-provenance to v3
  ([`74723cb`](https://github.com/camlloyd/oct-to-tiff/commit/74723cbd4206a5fd1650be4bd00db818a6fa831f))

- Bump docker/setup-buildx-action to v5
  ([`554f64e`](https://github.com/camlloyd/oct-to-tiff/commit/554f64ee9aa91cd61f1099e1a23ba227573e78b4))

- Restore TestPyPI URL in deployment status
  ([`1615185`](https://github.com/camlloyd/oct-to-tiff/commit/1615185de52699e9887d010acb7c77abce6b2627))

### Documentation

- **citation**: Update CITATION.cff
  ([`185aee0`](https://github.com/camlloyd/oct-to-tiff/commit/185aee0f63cbb710e3e3f5b2c5a34315d3fe0b5f))

- **readme**: Recommend installation via uv
  ([`9e6ae81`](https://github.com/camlloyd/oct-to-tiff/commit/9e6ae8163028145905cac658fe9c80b3e571e808))

### Refactoring

- **cli**: Prefer canonical name for `float`
  ([`4e02458`](https://github.com/camlloyd/oct-to-tiff/commit/4e024580132fd920deef98798d823c2be1a16c17))

### Testing

- **cli**: Add unit test for `boundaries_to_arrays`
  ([`e0ddb44`](https://github.com/camlloyd/oct-to-tiff/commit/e0ddb44a66cccebc3e2020ea292ee16dfeef8898))

- **cli**: Add unit test for `reshape_volume`
  ([`1cde0bd`](https://github.com/camlloyd/oct-to-tiff/commit/1cde0bda0e080c168eb8dc624808d430895d71ec))

- **cli**: Add unit tests for volume_metadata
  ([`96af8f9`](https://github.com/camlloyd/oct-to-tiff/commit/96af8f919cdb4ca2acede4864ed9a0e9245fdfd0))


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
