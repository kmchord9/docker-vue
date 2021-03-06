#!/bin/bash

DIR_VUE=/code
cd $DIR_VUE

DJANGO_SU_NAME=admin
DJANGO_SU_PASSWORD=mypass
DJANGO_DB_NAME=default
DJANGO_SU_EMAIL=admin@my.company
DJANGO_SETTING_MODULE=DJANGO_SETTING_MODULE

until ./manage.py inspectdb; do
  >&2 echo "Database is unavailable - sleeping"
  sleep 1
done

if [ ! -e db.sqlite3 ]; then
  if [ -e manage.py ]; then
    #init BD
    python manage.py makemigrations
    python manage.py migrate
    #create database user

  fi
else
  echo "db.sqlite3 found"
fi

cp /setup/setup.py /code/
python setup.py
python manage.py runserver 0.0.0.0:3000

