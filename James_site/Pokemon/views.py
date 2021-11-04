from django.shortcuts import render

# Create your views here.

from datetime import datetime
import pandas as pd
import os
import json


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

