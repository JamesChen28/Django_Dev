
# temp file for python test

import pandas as pd
import os
import json

path = os.getcwd()
path
pm_data = pd.read_csv(path + r'\James_site\data\Pokemon_Type.csv')
print(pm_data)

pm_data.iloc[0]

pm_data_1 = pm_data.to_json(force_ascii = False)
pm_data_1

pm_data.iloc[0].to_json(force_ascii = False)

pm_show = []
for i in range(len(pm_data)):
    pm_show.append(pm_data.iloc[i].to_json(force_ascii = False))

json.loads(pm_show[0])['屬性相剋表']




import pandas as pd
import os
import json

path = os.getcwd()
ac_data = pd.read_csv(path + r'\James_site\data\Animal_Crossing_Turnip.csv')

print(ac_data)

ac_data.iloc[0].to_json(force_ascii = False)
ac_show = []
for i in range(len(ac_data)):
    ac_show.append(ac_data.iloc[i].to_json(force_ascii = False))
ac_show
json.loads(ac_show[0])['上週\本週']
