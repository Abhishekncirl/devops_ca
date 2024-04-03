"""
Module for defining views.
"""
from django.shortcuts import render
from .models import Trav

def index(request):
    """
    View function for rendering the index page.
    """
    newest_trav = Trav.objects.order_by('title')[:15]
    context = {'newest_movies': newest_trav}
    return render(request, 'trav/index.html', context)
