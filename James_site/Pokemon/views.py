from django.shortcuts import render

# Create your views here.

from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    pm_data = load_pm_type()
    pm_show = []

    for i in range(len(pm_data)):
        pm_show.append(json.loads(pm_data.iloc[i].to_json(force_ascii = False)))

    return render(request, 'home.html', {
        'current_time': str(datetime.now()),
        'link': 'abc',
        'pm_show': pm_show,
    })

import pandas as pd
import os
import json

# path = os.getcwd()
# pm_data = pd.read_csv(path + r'\Pokemon\type.csv')
# pm_data_1 = pm_data.to_json(force_ascii = False)


def load_pm_type():
    path = os.getcwd()
    pm_data = pd.read_csv(path + r'\Pokemon\type.csv')
    # pm_data_1 = pm_data.to_json(force_ascii = False)
    print(pm_data)
    return pm_data

# print(load_pm_type)


