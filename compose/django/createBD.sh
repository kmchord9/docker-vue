#!/bin/bash

DIR_VUE=/code

if [ ! -e db.sqlite3 ]; then
  if [ -e manage.py ]; then
    #init BD
    python manage.py makemigrations && \
    python manage.py migrate
    #create database user
    python -c "import os; \
    import sys; \
    import django; \
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings'); \ 
    django.setup(); \
    from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
    get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser( \
        username='$DJANGO_SU_NAME', \
        email='$DJANGO_SU_EMAIL', \
        password='$DJANGO_SU_PASSWORD')"
  else
    echo "manage.py not found"
  fi
else
  echo "db.sqlite3 found"
fi

