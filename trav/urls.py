"""
Module for URL configuration.
"""
from django.urls import path
from . import views
     
urlpatterns = [
         path('', views.index, name='index'),
]
