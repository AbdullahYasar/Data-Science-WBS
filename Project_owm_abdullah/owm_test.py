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
lang_de = "de"
lang_en = "en"
API_key = "51d4430a6538d153d4c081015879b3a3"
city_name = input("City > ")  # Project for "Stuttgart", "Aachen", "Berlin"

def get_owm_data(city_name):

    for lang in lang_list:

        URL = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid="
               f"{API_key}&units=metric&lang={lang}")

        response = requests.get(URL)

        print(response)

        data = response.json()

        data_name = "data_"+str(city_name)+str(lang)+".json"

        with open(data_name, "w") as file:  # hilfe von ChatGBT
            json.dump(data, file)

        pprint(data)


def select_data(city_name, lang):
    data_name = "data_"+str(city_name)+str(lang)+".json"
    with open(data_name, mode="r", encoding="UTF-8") as file:
        data_owm = json.load(file)
    return data_owm



def insert_city(city_name):

    db = "./weather.db"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    data = (city_name,)
    sql = "INSERT INTO city(city_Name) VALUES (?);"
    

    # 4. Execute the SQL
    cursor.execute(sql, data)

    inserted_cityID = cursor.lastrowid

    # 6. Save the changes
    conn.commit()

    return inserted_cityID


def insert_weather():

    data = select_data(city_name, lang_de)
    data_en = select_data(city_name, lang_en)

    description_en = data_en["weather"][0]["description"]
    description_de = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    inserted_cityID = insert_city(city_name)
    

    db = "./weather.db"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    params = (inserted_cityID,description_en, description_de, temp, temp_min, temp_max)

    sql = "INSERT INTO weather(FK_cityID, description_en, description_de, temp, temp_min, temp_max) VALUES(?,?,?,?,?,?)"

    cursor.execute(sql, params)
    conn.commit()

def main():
    #city_name = input("City > ")  # Project for "Stuttgart", "Aachen", "Berlin"
    get_owm_data(city_name)


    # insert City
    insert_city(city_name)
    insert_weather()

    #inserted_cityID 



    print("Saved Successfully !")


if __name__ == "__main__":
    main()
