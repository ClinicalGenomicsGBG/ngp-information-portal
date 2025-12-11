# NGP Information Portal

## About
- [ ] todo


## Development


---
## First time setup


## Commands

### Generate a new secret_key for Django:
```sh
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" > src/.secret/secret_key2.txt
```