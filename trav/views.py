from django.http import HttpResponse
from .models import Trav
from django.shortcuts import render

     # Create your views here.
def index(request):
    newest_trav = Trav.objects.order_by('title')[:15]
    context = {'newest_movies': newest_trav}
    return render(request, 'trav/index.html', context)
