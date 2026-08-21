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

def result(request):
    a=int(request.GET['num1'])
    if(a>=80):
        return HttpResponse("Excellent")
    else:
        return HttpResponse("Good")
    
def greet(request,name):
    return HttpResponse(f"Hello {name} Welcome to Django")

def menu(request,dish):
    items={
        'sugar':"cost is 20rs/kg",
        'salt':"cost is 30rs/kg",
        'rice':"cost is 40rs/kg",
    }
    if dish in items:
        description=items[dish]
        return HttpResponse(f"<h1>{dish}</h1>"+description)
    else:
        return HttpResponse("Item not found")

def movie_finder(request,movie_name):
    movies={
        'inception':"A mind-bending thriller directed by Christopher Nolan.",
        'the godfather':"A classic crime film directed by Francis Ford Coppola.",
        'pulp fiction':"A cult classic directed by Quentin Tarantino.",
    }
    if movie_name in movies:
        description=movies[movie_name]
        return HttpResponse(f"<h1 style='color:green'>{movie_name}</h1>"+description)
    else:
        return HttpResponse(f"<h1 style='color:red'>Movie not found</h1>")

def recipe(request):
    food=request.GET.get("food")
    return HttpResponse(f"recipe available for food {food}")

def add(request):
    value1=request.GET.get("num1")
    value2=request.GET.get("num2")
    result=int(value1)+int(value2)
    return HttpResponse(f"Addition of {value1} and {value2} is {result}")
# Create your views here.
