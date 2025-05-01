#!/bin/sh

set -e

echo "Waiting for MySQL..."

until mysql -h "$MYSQL_HOST" -P "$MYSQL_PORT" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e 'SELECT 1'; do
  echo "MySQL not ready yet..."
  sleep 3
done

echo "MySQL is up!"

# Optional
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
