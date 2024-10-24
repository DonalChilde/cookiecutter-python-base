# Workflow

## Branches

- main is the release branch. This branch should always be the latest stable code.
- dev is the development branch. This is the unstable branch. When ready, code from this branch is merged into main for release.
- _other_ - branches for feature development and/or bug fixes. When ready, this code is merged into the dev branch.

## Typical work flow

- Make issue on github.
- Make a branch for the issue CHECK BRANCH SOURCE.
- `scriv create` to make a changelog fragment.
- Code to solve issue.
  - make sure tests, documentation, coverage, etc are passing
- make pull request to merge into dev branch.

## Release Checklist

Before a release, ensure all of the following are completed. This is usually started in the dev branch.

- [ ] All tests pass!
- [ ] Coverage is acceptable.
- [ ] Documentation is current.
- [ ] Changelog fragments are current
- [ ] Update version string in changelog.d/scriv.ini
- [ ] `scriv collect` to update changelog.
  - [ ] Do steps detailed in changelog comments.
- [ ] pull request to merge into main.
- [ ] Tag the new version on main. -> `git tag -a 0.0.0 -m "release 0.0.0"`
- [ ] Push the tag to origin -> `git push origin <tag name>`
- [ ] Create release on github.
  - [ ] Ensure correct tag and version are used.
  - [ ] Update release notes as needed.
