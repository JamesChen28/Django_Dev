from django.contrib import admin
from django.urls import path, re_path
# from django.conf.urls import include
from Animal_Crossing.views import animal_crossing_page

urlpatterns = [
    re_path('animal_crossing', animal_crossing_page, name='ac'),
]