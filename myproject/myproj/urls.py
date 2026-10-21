from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns=[
    # path('hello/',views.hello),
    # path('home/',views.home),
    # path('about/',views.about),
    # path('web/',views.web),
    # path('result/',views.result),
    # path('greet/<str:name>/',views.greet),
    # path('greet/<int:name>/',views.greet),
    # path('student/<int:id>/<str:name>/',views.student),
    # path('menu/<str:dish>/',views.menu),
    # path('movie_finder/<str:movie_name>/',views.movie_finder),
    # path('recipe/',views.recipe),
    # path('add/',views.add),
    # path('student1/',views.student1),
    # path('test/',views.test),
    # re_path(r'^userprofile/(?P<username>[\d]{2,4}+)/?$',views.userprofile),
    # re_path(r'^product/(?P<product_id>[\w]+)/$',views.productId),
    # path('login/',views.login),
    # path('',views.home),
    # path('about/',views.about),
    # path('content/',views.content),

    # path('blog/<slug:blog_slug>/',views.blog),
    # re_path(r'^result/(?P<id>\d+)/$',views.result)
    path('simpleform/',views.simpleform),
    path('templateform/',views.templateform),
    path('myform/',views.my_form_view, name='my_form'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
]