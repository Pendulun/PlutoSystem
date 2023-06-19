#!/bin/bash

export PYTHON=python3.10

# Missing dependencies
apt-get install -y libpq-dev postgresql-contrib lsb-release sudo
echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" \
     > /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
apt-get update
apt-get install -y postgresql-13
$PYTHON -m pip install poetry
chown -R postgres .

su -p postgres -s .github/workflows/frontend-check-entrypoint-postgres.sh
