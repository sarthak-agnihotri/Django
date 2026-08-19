from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")
def home(request):
    return HttpResponse("Welcome to Home Page")
def about(request):
    return HttpResponse("Welcome to About Page")

# Create your views here.
