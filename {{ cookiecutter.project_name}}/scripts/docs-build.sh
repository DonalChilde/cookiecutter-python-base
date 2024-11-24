#!/usr/bin/env bash

PROJECT_DIR = ${1:-{{ cookiecutter.package_name }}}

# Run from the project directory

# After code changes, and
# before each release at a minimum,
# generate the api files for autodoc.
./.venv/bin/sphinx-apidoc -f -o ./docs/source/documentation/api-generated/ ./src/$PROJECT_DIR/

# build the docs
./.venv/bin/sphinx-build -M html ./docs/source ./docs/build --fail-on-warning
