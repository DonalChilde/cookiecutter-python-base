# Changelog
<!-- markdownlint-disable MD024 -->
<!-- changelog-start -->

## [Unreleased](https://github.com/DonalChilde/cookiecutter-python-base/compare/0.0.3...dev)
<!-- Dont forget to:
    - Update the Unreleased compare version to latest release tag
    - Update compare/_previous_version_tag_
    - Delete <a></a> tag
    - Update issues and pull requests as needed.-->
<!-- Copy paste release notes below here -->
<!-- scriv-insert-here -->

## [0.0.3](https://github.com/DonalChilde/cookiecutter-python-base/compare/0.0.2...0.0.3) —  2024-11-02

### Whats Changed in 0.0.3

In this release, I added a functional example of a Typer cli app with tests, and working sphinx documentation. Also, some basic nox sessions, and project setup convenience scripts.

### Added

- Update dev docs and pyproject.toml[#94](https://github.com/DonalChilde/cookiecutter-python-base/pull/94)
  - closes
    - update pyproject.toml[#92](https://github.com/DonalChilde/cookiecutter-python-base/issues/92)
    - Document the development workflow[#21](https://github.com/DonalChilde/cookiecutter-python-base/issues/21)

- added some convenience scripts
  - closes
    - convenient shell scripts[#43](https://github.com/DonalChilde/cookiecutter-python-base/issues/43)

- Add a typer cli example[#112](https://github.com/DonalChilde/cookiecutter-python-base/pull/112)
  - closes
    - sphinx conf.py source_suffix[#111](https://github.com/DonalChilde/cookiecutter-python-base/issues/111)
    - fix cli testing[#110](https://github.com/DonalChilde/cookiecutter-python-base/issues/110)

### Changed

- Update project setup dev doc
  - closes
    - dev setup doc[#80](https://github.com/DonalChilde/cookiecutter-python-base/issues/80)

- A few small repairs[#108](https://github.com/DonalChilde/cookiecutter-python-base/pull/108)
  - closes
    - sphinx setup[#83](https://github.com/DonalChilde/cookiecutter-python-base/issues/83)
    - use project CHANGELOG.md in docs[#68](https://github.com/DonalChilde/cookiecutter-python-base/issues/68)
    - move cli in src[#106](https://github.com/DonalChilde/cookiecutter-python-base/issues/106)
    - add src pytest config option to pyproject.toml[#104](https://github.com/DonalChilde/cookiecutter-python-base/issues/104)
    - add example of github dependency to pyproject.toml[#103](https://github.com/DonalChilde/cookiecutter-python-base/issues/103)
    - Change cookie child dependency to Typer[#109](https://github.com/DonalChilde/cookiecutter-python-base/issues/109)
    - Edit release workflow version numbers[#102](https://github.com/DonalChilde/cookiecutter-python-base/issues/102)
    - Update github actions test runner[#99](https://github.com/DonalChilde/cookiecutter-python-base/issues/99)
    - add mark slow tests[#86](https://github.com/DonalChilde/cookiecutter-python-base/issues/86)

### Fixed

- fixed incorrect github compare link address.
- fixed github action for testing.

## [0.0.2](https://github.com/DonalChilde/cookiecutter-python-base/compare/v0.0.1...0.0.2) —  2024-10-23

### Whats Changed in 0.0.2

An incremental update testing out some workflow changes, and changelog format.

### Added

- Add scriv cookiecutter project.

  - Pull requests
    - [#90](https://github.com/DonalChilde/cookiecutter-python-base/pull/90)

  - closes
    - [#89](https://github.com/DonalChilde/cookiecutter-python-base/issues/89)

- Add and update the workflow dev doc
- Add a pyproject.toml
  - Add a src package so that version can be stored in __init__.py

  - Pull requests
    - [#93](https://github.com/DonalChilde/cookiecutter-python-base/pull/93)

  - closes
    - [#91](https://github.com/DonalChilde/cookiecutter-python-base/issues/91)
    - [#81](https://github.com/DonalChilde/cookiecutter-python-base/issues/81)
    - [#72](https://github.com/DonalChilde/cookiecutter-python-base/issues/72)

### Changed

- Use scriv to manage the changelog.

  - Pull requests
    - [#88](https://github.com/DonalChilde/cookiecutter-python-base/pull/88)

  - closes
    - [#87](https://github.com/DonalChilde/cookiecutter-python-base/issues/87)

## [v0.0.1](https://github.com/DonalChilde/cookiecutter-python-base/compare/v0.0.0...v0.0.1)

### What's Changed in v0.0.1

Many small improvements

### Added

- add-update release drafter and labeler ([#53](https://github.com/DonalChilde/cookiecutter-python-base/pull/53))
- 39 fix initial changelog format ([#40](https://github.com/DonalChilde/cookiecutter-python-base/pull/40))
- update git setup instructions ([#38](https://github.com/DonalChilde/cookiecutter-python-base/pull/38))
- changed name of tests action to Tests ([#37](https://github.com/DonalChilde/cookiecutter-python-base/pull/37))
- fix release drafter config file contents and name ([#36](https://github.com/DonalChilde/cookiecutter-python-base/pull/36))
- 28 add update changelog action ([#29](https://github.com/DonalChilde/cookiecutter-python-base/pull/29))
- add release drafter action ([#27](https://github.com/DonalChilde/cookiecutter-python-base/pull/27))
- add github labeler action, with custom labels ([#26](https://github.com/DonalChilde/cookiecutter-python-base/pull/26))
- read the docs setup instructions and config ([#24](https://github.com/DonalChilde/cookiecutter-python-base/pull/24))
- Drop old python version classifiers ([#19](https://github.com/DonalChilde/cookiecutter-python-base/pull/19))
- MIT license as default ([#18](https://github.com/DonalChilde/cookiecutter-python-base/pull/18))
- Change docs to markdown ([#16](https://github.com/DonalChilde/cookiecutter-python-base/pull/16))
- Add main as additional branch target ([#74](https://github.com/DonalChilde/cookiecutter-python-base/pull/74))
- Add project-setup to dev-docs ([#62](https://github.com/DonalChilde/cookiecutter-python-base/pull/62))
- Add a release checklist ([#61](https://github.com/DonalChilde/cookiecutter-python-base/pull/61))
- Add commit reference dev doc ([#58](https://github.com/DonalChilde/cookiecutter-python-base/pull/58))
- 55 add git command reference ([#56](https://github.com/DonalChilde/cookiecutter-python-base/pull/56))
- added changelog.md ([#54](https://github.com/DonalChilde/cookiecutter-python-base/pull/54))

### Changed

- Add version to Whats Changed header in CHANGELOG.md ([#65](https://github.com/DonalChilde/cookiecutter-python-base/pull/65))
- 47 fix label descriptions and colors ([#63](https://github.com/DonalChilde/cookiecutter-python-base/pull/63))
- 59 consolidate dev docs in cookiecutter ([#60](https://github.com/DonalChilde/cookiecutter-python-base/pull/60))

### Removed

- Delete update-changelog.yaml ([#57](https://github.com/DonalChilde/cookiecutter-python-base/pull/57))

### Fixed

- Create .gitkeep in docs/source/_static directory ([#67](https://github.com/DonalChilde/cookiecutter-python-base/pull/67))

## v0.0.0 - 2022-12-11

### Whats Changed in v0.0.0

This is the start of something....

### Added

- Project Start

<https://keepachangelog.com/en/1.0.0/>

<!-- changelog-end -->
