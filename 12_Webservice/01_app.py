# pip install fastapi
# pip install "uvicorn[standard]"
# To run the websevice (in terminal) : -->  uvicorn 01_app:app --reload

""" 
> http://127.0.0.1:8000
> www.mohamed.com

"""

from fastapi import FastAPI 


# 1. Create the FastAPI application
app = FastAPI() 



@app.get("/") # root addresse
def root():
    return {"message": "Welcome Mohamed"} 


@app.get("/greeting")
def greeting():
    return {"message": "Hallo Mohamed"}


# http://127.0.0.1:8000/items/21        -> 26
# http://127.0.0.1:8000/items/banana   -> Error
@app.get("/items/{item_id}")
def get_item(item_id:int):
    item_id += 5
    return {"Item": item_id}


# http://127.0.0.1:8000/getuserinfo?empid=1&name=thomas
# http://127.0.0.1:8000/getuserinfo?empid=2&name=2
# http://127.0.0.1:8000/getuserinfo?empid=apfel&name=thomas    -> Error
# 
@app.get("/getuserinfo")
def get_user_information(empid: int, name=str):

    print("The user Id is: ", empid)


    return {
        "user ID" : empid,
        "User name": name.upper()
    }