#!/bin/bash

set -euo pipefail

REMOTE="origin"
BRANCH="dev/add-mkdocs-project"
PULL=false
FORCE=false
REPO_DIR="/information_portal/ngp-information-portal"

NGINX_DIR="/var/www/mkdocs/"

for arg in "$@"; do
    case $arg in
        --pull)
            PULL=true
            ;;
        --force)
            FORCE=true
            ;;
        *)
            echo "Unknown option: $arg"
            echo "Usage: $0 [--pull] [--force]"
            exit 1
            ;;
    esac
done

cd "$REPO_DIR"


CHANGED=false
if $PULL; then
    echo "Pulling from git..."

    # Fetch and see if anything changed
    BEFORE=$(git rev-parse HEAD)
    git pull "$REMOTE" "$BRANCH" --quiet
    AFTER=$(git rev-parse HEAD)

    if [[ "$BEFORE" != "$AFTER" ]]; then
        CHANGED=true
        echo "Changes detected."
    else
        echo "No changes detected."
    fi
fi


if $FORCE || $CHANGED; then
    echo "Deploying..."
    /home/azureuser/.local/bin/uv run mkdocs build -cqf src/mkdocs.yml -d ../public-generated
    rm -rf "$NGINX_DIR"*
    cp -r "$REPO_DIR/public-generated/"* "$NGINX_DIR"
    chown -R nginx:nginx /var/www/mkdocs
    echo "Finished"
else
    echo "Nothing to deploy."
fi

