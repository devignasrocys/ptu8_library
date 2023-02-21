from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# index views
def index(request):
    return HttpResponse("Sveiki Studentai!")
