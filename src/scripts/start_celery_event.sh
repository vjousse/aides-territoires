#!/bin/bash

# This script is used by scalingo to start the the application
# It run every time the app container starts, for instance,
# after a deployment or when the container is restarted.

echo "Entering start celery event script"
export DJANGO_SETTINGS_MODULE=$1
if [ -z "$DJANGO_SETTINGS_MODULE" ]
  then
    echo "This script expects the DJANGO_SETTINGS_MODULE as first argument"
fi
echo "Using Django settings module: $DJANGO_SETTINGS_MODULE"
python manage.py compilemessages
celery -A core worker --events --loglevel info
echo "Completed start celery event script"