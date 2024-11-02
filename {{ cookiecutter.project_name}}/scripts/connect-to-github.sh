#!/usr/bin/env bash

# Run from the project directory

git remote add origin https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}.git
git push -u origin main
git push origin 0.0.0
git branch dev
git push -u origin dev
git checkout dev
