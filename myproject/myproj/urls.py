from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.hello),
    path('home/',views.home),
    path('about/',views.about),
    path('web/',views.web),
    path('result/',views.result),
    path('greet/<str:name>/',views.greet),
    # path('greet/<int:name>/',views.greet),
    path('menu/<str:dish>/',views.menu),
    path('movie_finder/<str:movie_name>/',views.movie_finder),
    path('recipe/',views.recipe),
    path('add/',views.add),
]