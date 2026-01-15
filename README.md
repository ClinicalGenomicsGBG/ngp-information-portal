# NGP Information Portal

## About
The NGP documentation portal will be the frontpage/www of the NGP project (www.genmed.se and ngp.genmed.se), and will contain news, documentation, project status (of NGP), links and general information.

There are several parts of the NGP, and many services/entrypoints for users (misc portals, including OOD, etc). This is a complex platform where information risk becoming scattered out on several different services/platforms, and thus hard to keep track of and up-to-date. The information portal will be a platform where we can provide users (and public) with centralized documentation, statistics, project progress (status), news, and general information for all of our services. The portal will also contain links to all of our platforms and support, etc.


## Development

### Setup

1. Set up **uv**:
    1. Install `uv`: https://docs.astral.sh/uv/getting-started/installation/
    1. Run `uv sync` to install dependencies and to set up the environment.


### Develop
1. Make changes.
1. Run `uv run mkdocs serve -f src/mkdocs.yml` to test the app locally.
    1. Alternatively serve `mkdocs` on a different port with: `uv run mkdocs serve -f src/mkdocs.yml --dev-addr <IP:PORT>`

### Build
- Run `uv run mkdocs build -cf src/mkdocs.yml -d ../public` to build the app.
  <u>**with**</u>
warnings.
- Run `uv run mkdocs build -cqf src/mkdocs.yml -d ../public` to build the app.
  <u>**without**</u> warnings


## Deploy
### Staging
- Create a PR to merge the "dev" branch into "staging".
- Once merged, run the build & deploy script @: `/information_portal/deploy.sh`.
todo:
- show drafts posts: https://squidfunk.github.io/mkdocs-material/plugins/blog/#config.draft

### Production
- Create a PR to merge the "staging" branch into "main".
- [ ] todo
