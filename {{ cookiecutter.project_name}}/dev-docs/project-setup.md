# Developer Setup

## New project with no existing repo
<!-- dev -->
***NOTE: Assumes Linux OS***

From the project directory:

### Individual commands

```bash
# Setup a virtual environment
# if using pyenv, pick your version
pyenv shell 3.11
python3 -m venv ./.venv
source ./.venv/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
pip3 install -U pip, wheel
# Install project dependencies 
pip3 install -e .[dev,lint,doc,vscode,testing]
# Create the local git repo, and install git hooks
git init
pre-commit install
pre-commit autoupdate
# Make initial commit. You may have to repeat the add and commit commands if git hooks modify files.
git add .
git commit -m "initial commit"
git tag -a 0.0.0 -m "initial commit tag"
# Link local git repo to a separately created new GitHub project.
git remote add origin https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}.git
git push -u origin master
git push origin 0.0.0
git branch dev
git push -u origin dev
git checkout dev
```

### Convenient one liners

```bash
# Pick your python version using pyenv - optional
pyenv shell 3.11
# Create the virtual environment and install dependencies
python3 -m venv ./.venv && source ./.venv/bin/activate && export PIP_REQUIRE_VIRTUALENV=true && pip3 install -U pip && pip3 install -e .[dev,lint,doc,vscode,testing]
```

```bash
# Create the local git repo, and install git hooks
git init && pre-commit install && pre-commit autoupdate
```

```bash
# Make initial commit. You may have to repeat this command if git hooks modify files
git add . && git commit -m "initial commit" && git tag -a 0.0.0 -m "initial commit tag"
```

```bash
# Link local git repo to a separately created new GitHub project.
git remote add origin https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}.git && git push -u origin master && git push origin 0.0.0 && git branch dev && git push -u origin dev && git checkout dev
```

### GitHub setup

- Project->settings->Actions-> allow actions read/write access
- Actions->Labeler_manual-> manually run workflow one time to establish Labels.

## Clone existing GitHub Project

TODO
<!-- end-dev -->