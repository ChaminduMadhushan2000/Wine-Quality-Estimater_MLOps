from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# 1. Load the trained model
model = joblib.load("model.joblib")

# 2. Define the input data format (what the user sends)
class Wine(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Wine Quality Prediction API is running!"}

@app.post("/predict")
def predict(wine: Wine):
    # Convert input data to format model expects
    data = [[
        wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid,
        wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide,
        wine.total_sulfur_dioxide, wine.density, wine.pH,
        wine.sulphates, wine.alcohol
    ]]
    
    # Make prediction
    prediction = model.predict(data)
    
    return {"predicted_quality": float(prediction[0])}