# {{ cookiecutter.friendly_name }}

<!-- badges-begin -->

<!-- pypi -->
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/{{ cookiecutter.project_name }}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }})][pypi status]
[![License](https://img.shields.io/pypi/l/{{ cookiecutter.project_name }})][license]

<!-- rtd -->
[![Documentation](https://img.shields.io/readthedocs/{{ cookiecutter.project_name }}/latest.svg?label=Read%20the%20Docs)][read the docs]

<!-- CI testing -->
[![CI - main](https://github.com/{{ cookiecutter.github_user }}/{{cookiecutter.project_name}}/actions/workflows/pytest-main.yaml/badge.svg?branch=main)][tests]
[![CI - dev](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/actions/workflows/pytest-dev.yaml/badge.svg?branch=dev)][tests]

<!-- Tools Used -->
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)][ruff]

[pypi status]: <https://pypi.org/project/{{ cookiecutter.project_name }}/>
[read the docs]: <https://{{ cookiecutter.project_name }}.readthedocs.io/>
[tests]: <https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/actions>
[pre-commit]: <https://github.com/pre-commit/pre-commit>
[ruff]: <https://github.com/astral-sh/ruff>

<!-- badges-end -->

## Features

- TODO

## Requirements

- TODO

## Quickstart

You can install _{{ cookiecutter.friendly_name }}_ via [pip] from [PyPI]:

```console
pip install {{ cookiecutter.project_name }}
```

You can also pip install from github:

```console
# You should replace 0.0.1 with the desired tagged version or branch name, eg. dev or main
"pip install {{ cookiecutter.project_name }}@git+http://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}@0.0.1"
```

## Usage

Please see the [documentation] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [DonalChilde]'s [cookiecutter-python-base] template, which was inspired by [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[DonalChilde]: https://github.com/DonalChilde
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[cookiecutter-python-base]: https://github.com/DonalChilde/cookiecutter-python-base
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/LICENSE
[contributor guide]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/CONTRIBUTING
[documentation]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/
