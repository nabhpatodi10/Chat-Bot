from fastapi import FastAPI
import uvicorn
from db.db import connect_to_mongo

app = FastAPI()
connect_to_mongo()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/storevector")
def storevector():
    pass

@app.post("/queryresult")
def queryResult():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
