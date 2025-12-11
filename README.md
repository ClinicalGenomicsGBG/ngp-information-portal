# NGP Information Portal

## About
- [ ] todo

## Development

### Setup

1. Set up **uv**:
    1. Install `uv`: https://docs.astral.sh/uv/getting-started/installation/
    1. Run `uv sync` to install dependencies and to set up the environment.
1. Set up **Django**:
    1. Create a secret:
        1. Create `src/.secrets/secret_key.txt` and add a secret key to it
        1. To generate a new secret key, run `scripts/generate_new_django_secret.sh`
6. Run `uv run python src/manage.py migrate` to apply all migrations
7. Run `uv run python src/manage.py runserver`,
   or `./dev_runserver.sh` to start the portal

## Commands

### Generate a new secret_key for Django:
```sh
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" > src/.secret/secret_key.txt
```