#!/usr/bin/env bash

# ------------------------------------
# Check pre-reqs installed & logged in
# ------------------------------------
# Check universal requirements
hash git 2>/dev/null || { echo >&2 "Git must be installed."; exit 1; }
hash heroku 2>/dev/null || { echo >&2 "Heroku CLI must be installed."; exit 1; }

# Check remote already added
if ! echo $(git remote) | grep -w "heroku" > /dev/null; then
    git remote add heroku https://git.heroku.com/ngsc-service-hours.git
fi

# TODO: not triggering..
# Check logged in to Heroku
if echo $(heroku auth:whoami) | grep "not logged in" > /dev/null; then
    echo >&2 "You must first login to Heroku using `heroku login`. Ask Eric (ecarell1@asu.edu) for his Heroku credentials."
    exit 1
fi


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

# Check different than Heroku
git fetch heroku master
if ! git diff --quiet master heroku/master; then
    echo >&2 "Nothing to deploy. Local is same as Heroku build."
    exit 1
fi

# -----------------------------------
# Deploy
# -----------------------------------

git push origin master
git push heroku master
