# NGP Information Portal

## About
- [ ] todo

## Development

### Setup

1. Set up **uv**:
    1. Install `uv`: https://docs.astral.sh/uv/getting-started/installation/
    1. Run `uv sync` to install dependencies and to set up the environment.


### Develop
1. Make changes.
1. Run `uv run mkdocs serve -cf src/mkdocs.yml` to test the app locally.


### Build
- Run `uv run mkdocs build -cf src/mkdocs.yml -d ../public` to build the app
  <u>**with**</u>
warnings.
- Run `uv run mkdocs build -cqf src/mkdocs.yml -d ../public` to build the app
  <u>**without**</u> warnings


## Deploy
### Staging
- Create a PR to merge the "dev" branch into "staging".
- Once merged, run the build & deploy script @: `/information_portal/deploy.sh`.

### Production
- Create a PR to merge the "staging" branch into "main".
- [ ] todo
