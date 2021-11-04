from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import include
from Home.views import home_page

urlpatterns = [
    re_path('', home_page, name='home'),
]