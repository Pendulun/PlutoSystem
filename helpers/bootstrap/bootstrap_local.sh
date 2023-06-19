#!/bin/bash

set -ex

PLUTO_TEST="${PLUTO_TEST:-true}"
user="${DB_USER:-postgres}"
pswd="${DB_PASSWORD:-changeme}"

host=localhost
port=5432
dbname=pluto
num_retries=3
sleeptime=5s

function exec_sql {
    sqlfpath=$1
    db=$2
    if [ ! -z "$db" ]; then
        dbstr="-d $db"
    fi
    PGPASSWORD="$pswd" psql -p $port -h "$host" --user "$user" $dbstr -a -f "$sqlfpath"
}

if [ "$PLUTO_TEST" = 'true' ]; then
    exec_sql drop_database.sql
fi

exec_sql create_database.sql
exec_sql create_tables.sql "$dbname"
if [ "$PLUTO_TEST" = 'true' ]; then
    exec_sql populate_tables_with_test_data.sql "$dbname"
fi

