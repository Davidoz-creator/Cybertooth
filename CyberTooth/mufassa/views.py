from django.shortcuts import render
from django.shortcuts import HttpResponse
from http.client import HTTPResponse
from .import models

# Create your views here.
def index (request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request,'contact')       
