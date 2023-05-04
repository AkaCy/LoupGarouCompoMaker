from django.shortcuts import render

from .models import Role

def home(request):
    return render(request, 'CompoMaker/home.html')

# Create your views here.
