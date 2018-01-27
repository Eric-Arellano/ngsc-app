#!/usr/bin/env bash

# -----------------------------------
# Check pre-reqs installed
# -----------------------------------
# Check universal requirements
hash git 2>/dev/null || { echo >&2 "Git must be installed."; exit 1; }
hash heroku 2>/dev/null || { echo >&2 "Heroku CLI must be installed."; exit 1; }


# -----------------------------------
# Check for project updates 
# -----------------------------------
# Check on master branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != "master" ]]; then
  git checkout master
fi

# Check for clean local
if ! git diff-index --quiet HEAD --; then
    echo >&2 "Commit before trying to push. Local branch should be clean."
    exit 1
fi

# Update from master
git fetch origin master
git merge --ff-only  # abort if merge required


# -----------------------------------
# Deploy
# -----------------------------------

git push origin master
git push heroku master