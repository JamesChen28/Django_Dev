from django.shortcuts import render

# Create your views here.

from datetime import datetime
import pandas as pd
import os
import json


def home_page(request):
    pm_data = load_pm_type()
    pm_show = []

    # pm_page = pokemon_page(request)

    for i in range(len(pm_data)):
        pm_show.append(json.loads(pm_data.iloc[i].to_json(force_ascii = False)))

    return render(request, 'home.html', {
        'current_time': str(datetime.now()),
        'link': 'abc',
        'pm_show': pm_show,
        # 'pm_page': pm_page,
    })



# path = os.getcwd()
# pm_data = pd.read_csv(path + r'\Pokemon\type.csv')
# pm_data_1 = pm_data.to_json(force_ascii = False)


def load_pm_type():
    path = os.getcwd()
    pm_data = pd.read_csv(path + r'\data\Pokemon_Type.csv')
    # pm_data_1 = pm_data.to_json(force_ascii = False)
    return pm_data

print(load_pm_type)


def pokemon_page(request):
    x = 'pokemon page'
    pm_data = load_pm_type()
    pm_show = []

    # pm_page = pokemon_page(request)

    for i in range(len(pm_data)):
        pm_show.append(json.loads(pm_data.iloc[i].to_json(force_ascii = False)))

    return render(request, 'pokemon.html', {
        'current_time': str(datetime.now()),
        'link': x,
        'pm_show': pm_show,
    })

def animal_crossing_page(request):
    x = 'animal page'

    ac_data = load_animal_crossing()
    ac_show = []
    for i in range(len(ac_data)):
        ac_show.append(json.loads(ac_data.iloc[i].to_json(force_ascii = False)))
    return render(request, 'animal_crossing.html', {
        'current_time': str(datetime.now()),
        'link': x,
        'ac_show': ac_show,
    })

def load_animal_crossing():
    path = os.getcwd()
    ac_data = pd.read_csv(path + r'\data\Animal_Crossing_Turnip.csv')
    return ac_data

print(load_animal_crossing)
