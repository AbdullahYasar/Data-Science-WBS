from fastapi import FastAPI 


# 1. Create the FastAPI application
app = FastAPI() 



@app.get("/") # root addresse
def root():
    return {"message": "Welcome Mohamed"} 


@app.get("/greeting")
def greeting():
    return {"message": "Hallo Mohamed"}