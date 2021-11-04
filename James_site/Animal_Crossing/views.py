from django.shortcuts import render

# Create your views here.

from datetime import datetime
import pandas as pd
import os
import json

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
