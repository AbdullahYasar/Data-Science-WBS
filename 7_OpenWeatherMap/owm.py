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
lang_de = lang_list[0]
lang_en = lang_list[1]

API_key = "51d4430a6538d153d4c081015879b3a3"


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


def select_data(lang, city_name):
    data_name = "data_" + str(city_name) + {lang} + ".json"
    with open(data_name, mode="r", encoding="UTF-8") as file:
        data_owm = json.load(file)
    return data_owm

def database_mng():

    db = "./weather"
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    return cursor


def insert_city(city_name):

    # 3. SQL Statement

    cursor = database_mng()

    sql = "INSERT INTO city(CityName) VALUES (?);"
    data = (city_name,)

    # 4. Execute the SQL
    cursor.execute(sql, data)

    inserted_cityID = cursor.lastrowid

    # 6. Save the changes
    conn.commit()

    return inserted_cityID


def insert_weather_de():

    data = select_data(lang_de)
    data_en = select_data(lang_en)

    description_en = data_en["weather"]["description"]
    description_de = data["weather"]["description"]
    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    # FK_cityID =
    cursor = database_mng()

    database_mng()

    params = (inserted_cityID,description_en, description_de, temp, temp_min, temp_max)

    sql = "INSERT INTO weather(FK_cityID,description_en, description_de, temp, temp_min, temp_max) VALUES(?,?,?,?,?)"

    cursor.execute(sql, params)
    conn.commit()


def insert_description_en():

    cursor = database_mng()
    data = select_data(lang_en)

    description_en_new = data["weather"]["description"]

    database_mng()

    params = (description_en_new, )

    sql = "UPDATE weather SET description_en = ?  "

    cursor.execute(sql, params)
    conn.commit()


def main():
    city_name = input("City > ")  # Rostock

    # Insert City
    inserted_cityID = insert_city(city_name)

    print("Saved Successfully !")


if __name__ == "__main__":
    main()
