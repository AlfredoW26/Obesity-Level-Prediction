# Alfredo Winston - 2702297776

import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from obesity_data import obesity_data

app = FastAPI()
with open("xgb_model.pkl", "rb") as f:
    classifier = pickle.load(f)

with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.get('/')
def index():
    return{'message': 'Hello, Student!'}

@app.post('/predict')
def predict(data: obesity_data):
    data_dict = data.dict()
    df = pd.DataFrame([data_dict])

    # transformasi fitur
    X_processed = preprocessor.transform(df)

    # prediksi
    prediction = classifier.predict(X_processed)
    result = label_encoder.inverse_transform(prediction)[0]
    # result = str(prediction[0])

    return {
        'prediction': result
    }


if __name__ == "__main__":
    uvicorn.run(app, host ="127.0.0.1", port=8000)

