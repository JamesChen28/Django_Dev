from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import include
from Pokemon.views import pokemon_page

urlpatterns = [
    re_path('pokemon', pokemon_page, name='pm'),
]