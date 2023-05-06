from django.urls import re_path,include
from django.contrib import admin
from . import views
urlpatterns = [
    re_path(r'^$', views.home,name='home'),
    re_path(r'imageprocess', views.imageprocess,name='imageprocess'),
]
