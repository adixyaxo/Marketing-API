# from src.api.service import GET
from src.api.service import removeDuplicates
from src.api.service import getOptions
from src.config.database import DF
from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO
from fastapi.exceptions import HTTPException
from src.services.handle_routes import handle_uploads
# print(GET.getName(GET.getAudience(GET.getType(DF,"Email"),"Men 18-24"),"Innovate Industries"))

app = FastAPI()

@app.get("/")
def read_root():
    return getOptions()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await handle_uploads(file=file)

# CREATE
@app.post("/create")
def create_item(item: dict):
    return {"item":item}

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



