"""
Module for registering models with the Django admin interface.
"""
from django.contrib import admin
from .models import Trav

# Register your models here.

admin.site.register(Trav)