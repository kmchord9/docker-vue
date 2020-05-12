# -*- coding: utf-8 -*-

import os
import sys
import django

DJANGO_DB_NAME="default"
DJANGO_SU_NAME="admin"
DJANGO_SU_EMAIL="admin@my.company"
DJANGO_SU_PASSWORD="mypass"
DJANGO_SETTING_MODULE="DJANGO_SETTING_MODULE"

DATABASE_KEY = { 'phy': ['温度', '湿度', '気圧'],
                 'dev': ['BME280', 'ADT7410', 'MAX31855'],
                 'plc': ['部屋001', '部屋002'] }

#データベースのセットアップ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup() 

from django.contrib.auth.management.commands.createsuperuser import get_user_model 
get_user_model()._default_manager.db_manager(DJANGO_DB_NAME).create_superuser( 
  username = DJANGO_SU_NAME, 
  email = DJANGO_SU_EMAIL, 
  password = DJANGO_SU_PASSWORD)

from api.models import *

for name in DATABASE_KEY['phy']:
  res,_ = Physics.objects.get_or_create(physics=name)

for name in DATABASE_KEY['dev']:
  res,_ = Device.objects.get_or_create(device=name)

for name in DATABASE_KEY['plc']:
  res,_ = Place.objects.get_or_create(place=name)



