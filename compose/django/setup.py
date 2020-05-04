# -*- coding: utf-8 -*-

import os
import sys
import django

DJANGO_DB_NAME="default"
DJANGO_SU_NAME="admin"
DJANGO_SU_EMAIL="admin@my.company"
DJANGO_SU_PASSWORD="mypass"
DJANGO_SETTING_MODULE="DJANGO_SETTING_MODULE"

#データベースのセットアップ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup() 

from django.contrib.auth.management.commands.createsuperuser import get_user_model 
get_user_model()._default_manager.db_manager(DJANGO_DB_NAME).create_superuser( 
  username = DJANGO_SU_NAME, 
  email = DJANGO_SU_EMAIL, 
  password = DJANGO_SU_PASSWORD)