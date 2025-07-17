
# Iris Flower Predictor API with FastAPI

This project demonstrates how to deploy a machine learning model using FastAPI.

## Features
- Trains a `RandomForestClassifier` on the Iris dataset.
- Serves predictions via a FastAPI REST API.
- Uses Swagger UI for easy API testing.
- Supports real-time ML inference with validated JSON input.
## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Train the model:
   ```
   python model/train_model.py
   ```

3. Run the API:
   ```
   uvicorn app.main:app --reload
   ```

4. Access Swagger UI at:
   ```
   http://127.0.0.1:8000/docs
   ```

## Example API Request
POST `/predict`  
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Response
```json
{
  "species": "setosa"
}
```
