"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import LogViewSet, PhysicsViewSet, DeviceViewSet, PlaceViewSet
from api.views import MainView

router = routers.DefaultRouter()
router.register(r'logs', LogViewSet)
router.register(r'physics', PhysicsViewSet)
router.register(r'device', DeviceViewSet)
router.register(r'place', PlaceViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('', MainView.as_view),

]

admin.site.site_header = '気温と湿度の変化'
