from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, this is the dashboard index page.") 

# Create your views here.
