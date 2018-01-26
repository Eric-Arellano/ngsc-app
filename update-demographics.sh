#!/usr/bin/env bash

# -----------------------------------
# Check pre-reqs installed
# -----------------------------------
hash git 2>/dev/null || { echo >&2 "Git must be installed."; exit 1; }
hash heroku 2>/dev/null || { echo >&2 "Heroku CLI must be installed."; exit 1; }
hash jq 2>/dev/null || { echo >&2 "JQ must be installed. See https://stedolan.github.io/jq/"; exit 1; }


# -----------------------------------
# Check for project updates 
# -----------------------------------
# Check on master branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != "master" ]]; then
  echo "Change to master branch."
  exit 1
fi

Check for clean local
if ! git diff-index --quiet HEAD --; then
    echo "Make sure the branch is clean before running this script."
    exit 1
fi

Update from master
git fetch origin master
git merge --ff-only  # abort if merge required


# -----------------------------------
# Get new student info & save
# -----------------------------------
# Get student JSON
student_info=$(curl http://ngsc-app.org/api/demographics/all_students --silent)

# Save to file
echo $student_info | jq . > backend/src/student_ids.py  # pretty-prints json to file
first_line="student_ids = {"
sed -i '.bak' "1s/.*/$first_line/" backend/src/student_ids.py  # replaces first line with $first_line

# -----------------------------------
# Redeploy
# -----------------------------------
git add backend/src/student_ids.py
git commit -m 'update demographics'
git push origin master
git push heroku master
