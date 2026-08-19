from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")
def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")
def about(request):
    return HttpResponse("<h1>Welcome to About Page</h1>")
def web(request):
    name="Django"
    return HttpResponse(f"This is a {name} Web Framework")

# Create your views here.
