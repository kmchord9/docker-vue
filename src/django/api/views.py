from django.shortcuts import render
import django_filters
from django_filters import rest_framework as filters
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import ModelChoiceFilter
import json
from django.http.response import JsonResponse
from rest_framework.response import Response
from .models import *

# Create your views here.

class LogSerializer(serializers.ModelSerializer):  
  class Meta:
    model = Log
    fields = '__all__'

class LogFilter(django_filters.FilterSet):
  created_at = filters.DateTimeFilter(lookup_expr='date')
  created_gt = filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
  physics = filters.NumberFilter(field_name='physics',lookup_expr='exact')
  device = filters.NumberFilter(field_name='device',lookup_expr='exact')
  place = filters.NumberFilter(field_name='place',lookup_expr='exact')
  
  class Meta:
    model = Log
    fields = ['created_at', 'created_gt', 'physics', 'device', 'place']

class LogViewSet(viewsets.ModelViewSet):
  queryset = Log.objects.all().order_by("created_at")

  serializer_class = LogSerializer
  filter_class = LogFilter

  authentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes= (IsAuthenticated,)

class PlaceSerializer(serializers.ModelSerializer):  
  class Meta:
    model = Place
    fields = '__all__'

class PlaceViewSet(viewsets.ModelViewSet):
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

  authentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes= (IsAuthenticated,)

class MainView(LoginRequiredMixin, TemplateView):
  template_name = 'index.html'


class UserViewSet(viewsets.ViewSet):
  def list(self, request):
    phys = list(Physics.objects.all().values_list())
    devs = list(Device.objects.all().values_list())
    plas = list(Place.objects.all().values_list())

    relate = {
            'physics':{ phy[1]: phy[0] for phy in phys },
            'device':{ dev[1]: dev[0] for dev in devs },
            'place':{ pla[1]: pla[0] for pla in  plas }
            }
    #json_data = json.dumps(relate, ensure_ascii=False)

    return Response(relate)
