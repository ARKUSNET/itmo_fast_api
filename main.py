import joblib
import uvicorn

import numpy as np
import pandas as pd
import src.utils as utl
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

with open("rf_fitted.pkl", 'rb') as file:
    model = joblib.load(file)


class ModelRequestData(BaseModel):
    lat: float
    lon: float
    total_square: float
    rooms: float
    floor: float
    is_studio: float
    floor_category: float


class Result(BaseModel):
    result: float


@app.get("/health")
def health():
    return JSONResponse(content={"message": "It's alive!"}, status_code=200)


@app.get("/predict_get")
def preprocess_data_get():
    input_data = utl.get_default_data()
    input_df = pd.DataFrame(input_data, index=[0])
    result = model.predict(input_df)[0]
    return JSONResponse(content=round(np.exp(result), 3), status_code=200)


@app.post("/predict_post", response_model=Result)
def preprocess_data_post(data: ModelRequestData):
    input_data = data.dict()
    input_df = pd.DataFrame(input_data, index=[0])
    result = model.predict(input_df)[0]
    return Result(result=round(np.exp(result), 3))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)