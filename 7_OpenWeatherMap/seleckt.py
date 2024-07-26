
import json
import os
from pathlib import Path
from pprint import pprint

os.chdir(Path(__file__).parent)




# data_name = "data_Stuttgartde.json"
# with open(data_name, mode="r", encoding="UTF-8") as file:
#     data = json.load(file)



def select_data(city_name, lang):

    data_name = "data_"+str(city_name)+str(lang)+".json"
    
    with open(data_name, mode="r", encoding="UTF-8") as file:
        data_owm = json.load(file)
    return data_owm


data = select_data("Stuttgart", "de")
pprint(data)