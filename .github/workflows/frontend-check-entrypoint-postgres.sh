#!/bin/bash

set -ex

pg_ctlcluster 13 main start
psql -c '\du'
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
