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

su -p postgres
pg_ctlcluster 13 main start
psql -c "ALTER USER postgres PASSWORD 'changeme';"
cd /root/helpers/bootstrap
./bootstrap_local.sh
cd ../../

# Start backend
cd backend/pluto
$PYTHON -m poetry env use 3.10
. .venv/bin/activate
poetry install
export HOST=localhost
export PORT=5000
export DB_USER=postgres
export DB_PASSWORD=changeme
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=pluto
nohup python3 pluto/main.py &
cd ../../

# Start frontend
cd frontend
unset PORT
pnpm install
nohup pnpm start &

# Run cypress
npm run env -- cypress install
npm run env -- cypress run