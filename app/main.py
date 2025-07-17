
from fastapi import FastAPI
from app.schemas import IrisFeatures
import joblib
import numpy as np

app = FastAPI(title="Iris Flower Predictor")

model = joblib.load("app/model.pkl")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Predictor API!"}

@app.post("/predict")
def predict_species(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width,
                      features.petal_length, features.petal_width]])
    prediction = model.predict(data)
    species = ["setosa", "versicolor", "virginica"]
    return {"species": species[prediction[0]]}
