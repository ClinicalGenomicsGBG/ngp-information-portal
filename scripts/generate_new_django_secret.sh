#!/usr/bin/env bash
set -euo pipefail

if ! command -v uv >/dev/null 2>&1; then
    echo "✖ 'uv' is not installed or not in PATH."
    exit 1
fi

REPOSITORY_NAME="ngp-information-portal"

# Make sure we're in a git repo, and the correct git repo.
if ! PROJECT_ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null)"; then
    echo "✖ Script must be executed from a git repository."
    exit 1
fi
if [ "$(basename "$PROJECT_ROOT_DIR")" != "$REPOSITORY_NAME" ]; then
    echo "✖ This script must be executed from the \"$REPOSITORY_NAME\" repository."
    exit 1
fi

SECRETS_DIR="$PROJECT_ROOT_DIR/src/.secrets"
SECRETS_FILE="$SECRETS_DIR/secret_key.txt"

# Create the secrets' directory if it does't already exist.
if [ ! -d "$SECRETS_DIR" ]; then
    mkdir -p "$SECRETS_DIR"
fi

# Generate a new Django secret and write it to file
uv run python - <<'EOF' > "$SECRETS_FILE"
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
EOF

