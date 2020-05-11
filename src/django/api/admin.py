from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Physics)
class PhysicsAdmin(admin.ModelAdmin):
  pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
  pass

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
  pass

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
  pass