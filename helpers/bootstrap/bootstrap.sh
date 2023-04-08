#!/bin/ash

set -e

user="$DB_USER"
pswd="$DB_PASSWORD"

host=pluto_pg
dbname=pluto
num_retries=3
sleeptime=5s

function exec_sql {
    sqlfpath=$1
    db=$2
    if [ ! -z "$db" ]; then
        dbstr="-d $db"
    fi
    PGPASSWORD="$pswd" psql -h "$host" --user "$user" $dbstr -a -f "$sqlfpath"
}

function sleepy_doopy {
    echo "Im awake, Im awake..."
    echo "Sleeping for $sleeptime..."
    sleep "$sleeptime"
}

if [ "$PLUTO_TEST" = 'true' ]; then
    exec_sql drop_database.sql
fi

exec_sql create_database.sql
exec_sql create_tables.sql "$dbname"
if [ "$PLUTO_TEST" = 'true' ]; then
    exec_sql populate_tables_with_test_data.sql "$dbname"
fi

while true; do
    sleepy_doopy
done
