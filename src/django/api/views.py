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
from .models import Log

# Create your views here.

class LogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Log
    fields = '__all__'

class LogFilter(django_filters.FilterSet):
  created_at = filters.DateTimeFilter(lookup_expr='date')
  created_gt = filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
  device = filters.CharFilter(field_name='device',lookup_expr='exact')
  place = filters.CharFilter(field_name='place',lookup_expr='exact')
  
  class Meta:
    model = Log
    fields = ['created_at', 'created_gt', 'device', 'place']

class LogViewSet(viewsets.ModelViewSet):
  queryset = Log.objects.all().order_by("created_at")

  serializer_class = LogSerializer
  filter_class = LogFilter

  authentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes= (IsAuthenticated,)

class MainView(LoginRequiredMixin, TemplateView):
  template_name = 'index.html'

