
#%%
import os
import json
from pathlib import Path
import pprint
os.chdir(Path(__file__).parent)

with open("./data_Stuttgartde.json", mode = "r", encoding = "UTF-8") as file:
    data = json.load(file)

pprint.pprint(data)

import sqlite3

city_name = "Stuttgart"

db = "./weather.db"
conn = sqlite3.connect(db)
cursor = conn.cursor()



num = 2
par = (num, )

sql = "DELETE FROM city WHERE city_ID = ?"

cursor.execute(sql, par)

conn.commit()
rows = cursor.fetchall()

print(rows)

#%%


sql = "INSERT INTO city(City_Name) VALUES (?);"
data = ("Stuttgart", )

# 4. Execute the SQL
cursor.execute(sql, data)

inserted_cityID = cursor.lastrowid

# 6. Save the changes
conn.commit()

print(inserted_cityID)
