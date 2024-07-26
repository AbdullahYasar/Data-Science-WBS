import os
from pathlib import Path
import sqlite3
from datetime import datetime
import requests
from pprint import pprint
import json

os.chdir(Path(__file__).parent)

city_list = ["Stuttgart", "Aachen", "Berlin"]
lang_list = ["de", "en"]
API_key = "51d4430a6538d153d4c081015879b3a3"


def get_owm_data():

    for city_name in city_list:
        for lang in lang_list:

            # city_name = "Stuttgart"
            # country_code = "de"

            URL = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid="
                   f"{API_key}&units=metric&lang={lang}")

            response = requests.get(URL)

            print(response)

            data = response.json()

            data_name = "data_"+str(city_name)+str(lang)+".json"

            with open(data_name, "w") as file:  # hilfe von ChatGBT
                json.dump(data, file)

            pprint(data)



def database_mng():

    db = "./weather"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()


def insert_city_name():

    for city_name in city_list:

        data_name = "data_"+str(city_name)+"de"+".json"

        with open(data_name, mode = "r", encoding = "UTF-8") as file: 
            data_owm = json.load(file)

        city = data_owm["name"]

        print(city)

        db = "./weather"
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        sql = "INSERT INTO city(city_Name) VALUES (?) "
        params = (city,)

        cursor.execute(sql, params)
        conn.commit()

    
def insert_weather():
    for city_name in city_list:

        data_name = "data_" + str(city_name) + "de" + ".json"
        with open(data_name, mode="r", encoding = "UTF-8") as file:
            data_owm = json.load(file)

            # description_en = data_owm[]
            # description_de = data_owm[]
            temp = data_owm["main"]["temp"]
            temp_min = data_owm["main"]["temp_min"]
            temp_max = data_owm["main"]["temp_max"]
            # FK_cityID

            database_mng()

            params = (FK_cityID, temp, temp_min, temp_max)

            sql = "INSERT INTO weather(FK_cityID,  temp, temp_min, temp_max) VALUES(?,?,?,?)"

            cursor.execute(sql, params)
            conn.commit()


















