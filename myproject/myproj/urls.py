from django.urls import path, re_path
from . import views

urlpatterns=[
    path('hello/',views.hello),
    path('home/',views.home),
    path('about/',views.about),
    path('web/',views.web),
    path('result/',views.result),
    path('greet/<str:name>/',views.greet),
    # path('greet/<int:name>/',views.greet),
    path('student/<int:id>/<str:name>/',views.student),
    path('menu/<str:dish>/',views.menu),
    path('movie_finder/<str:movie_name>/',views.movie_finder),
    path('recipe/',views.recipe),
    path('add/',views.add),
    # re_path(r'^userprofile/(?P<username>[\d]{2,4}+)/?$',views.userprofile),
    # re_path(r'^product/(?P<product_id>[\w]+)/$',views.productId),
    

]