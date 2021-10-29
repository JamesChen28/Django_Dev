from django.contrib import admin
from django.urls import path
# from django.conf.urls import include
from Pokemon.views import hello_world, pokemon_page

urlpatterns = [
    path('', pokemon_page, name='pokemon'),
]