from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Home Page of Blog App</h1>')

def about(request):
    return HttpResponse('<h1>Home Page of Blog About</h1>')
