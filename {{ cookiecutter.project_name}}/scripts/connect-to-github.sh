#!/usr/bin/env bash
GITHUB_USER=${1:-{{ cookiecutter.github_user }}}
PROJECT_NAME = ${2:-{{ cookiecutter.project_name }}}
# Run from the project directory

git remote add origin https://github.com/$GITHUB_USER/$PROJECT_NAME.git
git push -u origin main
git push origin 0.0.0
git branch dev
git push -u origin dev
git checkout dev
