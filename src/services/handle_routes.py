from fastapi import UploadFile, File
from fastapi.exceptions import HTTPException
from io import BytesIO
import pandas as pd
from src.services.data_cleaning import get_unique_values
async def handle_uploads(file:UploadFile=File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="File must be a CSV")

    try:
        # 2. Read file content into memory
        contents = await file.read()

        # 3. Parse CSV using pandas via BytesIO
        # This avoids saving the file to disk
        df = pd.read_csv(BytesIO(contents))
        # 4. Convert to JSON (list of dictionaries)
        data = df.to_dict("records")
        columns:list = df.columns.tolist()

        return {"data":columns}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing CSV: {str(e)}")
    finally:
        await file.close()


