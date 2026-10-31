from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    # path('register/',views.register),
    # path('login/',views.login_view),
    # path('contact/',views.contact),
    # path('success/',views.success,name='success')
    path('feedback/',views.feedback,name='feedback'),
    path('success/',views.success,name='success'),
]