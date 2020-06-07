#!/bin/bash
# wait-for-db.sh

set -e

cmd="$@"
python ./manage.py makemigrations

until python ./manage.py migrate; do
    >&2 echo "DB is unavailable"
    sleep 1
done

>&2 echo "DB is up"

exec $cmd