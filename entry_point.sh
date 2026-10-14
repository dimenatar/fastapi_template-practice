#!/bin/sh

counter=0

echo "DB_HOST:: $DB_HOST; DB_PORT:: $DB_PORT"

while ! nc -z "$DB_HOST" "$DB_PORT" && [ $counter -lt 10 ]; do
  sleep 1
  echo "Waiting for postgres $counter"
  counter=$((counter + 1))
done

exec "$@"