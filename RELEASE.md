# How to make a SATRE Release

## Prerequisites

- [ ] Update architecture links if necessary
- [ ] If this is a major change add document with itemised changes from previous major version
- [ ] Check [open PRs](https://github.com/sa-tre/satre-specification/pulls) for anything relevant
- [ ] Check [project board](https://github.com/orgs/sa-tre/projects/2) for any remaining tasks for this version
- [ ] Do a final read through of the latest published version https://satre-specification.readthedocs.io/en/latest/
- [ ] Update the `Releases` section of the index page with a very brief summary of the changes https://github.com/sa-tre/satre-specification/blob/main/docs/source/index.md#releases

## Making the release

- Go to https://github.com/sa-tre/satre-specification/releases
- Click `Draft new release`
  - [ ] Tag: In the dropdown click in the `Search or create a new tag` field, enter a new tag `vX.Y.Z`, and click `Create new tag`
  - [ ] Target: Leave as `main`
  - [ ] Release title: `Version X.Y.Z`
  - [ ] Release notes: write something (don't autogenerate because it'll give a useless list of PRs)
  - [ ] Release label: leave as `latest`
  - `Save draft` to check everything

You can return to the draft to make further changes

## The final step

- Go to https://github.com/sa-tre/satre-specification/releases
- Click the edit icon on the draft
- [ ] Click `Publish release` when ready: this should automatically create the git tag at the _current_ state of the `main` branch

Visit https://app.readthedocs.org/projects/satre-specification/ to check on the build status
