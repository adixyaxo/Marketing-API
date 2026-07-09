# from src.api.service import GET
from src.api.service import removeDuplicates
from src.api.service import getOptions
from src.config.database import DF
from fastapi import FastAPI
# print(GET.getName(GET.getAudience(GET.getType(DF,"Email"),"Men 18-24"),"Innovate Industries"))

app = FastAPI()

@app.get("/")
def read_root():
    return getOptions()

# CREATE
@app.post("/create")
def create_item(item: dict):
    return item
# READ
@app.get("/read")
def read_item():
    return {"message": "Reading item"}
# UPDATE
@app.put("/update")
def update_item(item: dict):
    return item
# DELETE
@app.delete("/delete")
def delete_item():
    return {"message": "Deleting item"}



