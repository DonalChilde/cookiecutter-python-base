#!/usr/bin/env bash

# Run from the project directory
# this is only ment to be run on a new project

# Create the local git repo, and install git hooks
git init --initial-branch=main
pre-commit install
pre-commit autoupdate

# run these before the git hooks to try to avoid
# having the first commit fail
black ./src ./tests .
isort ./src ./tests .

# Make initial commit. You may have to repeat the add and commit commands if git hooks modify files.
git add .
git commit -m "initial commit"
git tag -a 0.0.0 -m "initial commit tag"
