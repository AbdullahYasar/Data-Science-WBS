import os 
from pathlib import Path 
import sqlite3
os.chdir(Path(__file__).parent)

import databasemanager as dbm

DB_NAME = "./essohanam.db"



# 1. DB Connection
conn = sqlite3.connect(DB_NAME)

# 2. Create a cursor
cursor = conn.cursor() 


def select_data():
  

    # 3. SQL Statement
    sql = "SELECT * FROM city;"

    # 4. Execute the SQL
    cursor.execute(sql)

    # 5. Get the rows
    rows = cursor.fetchall()


    for row in rows:
        print(row)



def insert_city(city_name):


    # 3. SQL Statement
    sql = "INSERT INTO city(CityName) VALUES (?);"
    data = (city_name,)

    # 4. Execute the SQL
    cursor.execute(sql, data)

    inserted_cityID = cursor.lastrowid

    # 6. Save the changes
    conn.commit()

    return inserted_cityID


def insert_participant(first_name, last_name, inserted_cityID):
    # 3. SQL Statement
    sql = "INSERT INTO participant(FirstName, LastName, FK_CityID) VALUES (?,?,?);"
    data = (first_name, last_name, inserted_cityID)

    # 4. Execute the SQL
    cursor.execute(sql, data)


    # 6. Save the changes
    conn.commit()



def main():

    
    city_name = input("City > ")  # Rostock
    first_name = input("First Name > ")  # 
    last_name = input("Last Name > ")  # 

    select_data()

    # Insert City
    inserted_cityID = insert_city(city_name)


    # Insert Participant
    insert_participant(first_name, last_name, inserted_cityID)

    dbm.insert_data(sql, data)


    rows = dbm.select_data()

    print("Saved Successfully !")



if __name__ == "__main__":
    main()