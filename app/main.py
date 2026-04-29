from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib


app = FastAPI(title="Student Score Prediction API")

model = joblib.load("app/model/student_score_model.pkl")


class StudentInput(BaseModel):
    hours_studied: float
    sleep_hours: float
    attendance_rate: float
    previous_score: float


@app.get("/health")
def health_check():
    return {
        "message": "Student Score Prediction API is running"
    }


@app.post("/predict")
def predict_score(student: StudentInput):
    input_data = pd.DataFrame({
        "hours_studied": [student.hours_studied],
        "sleep_hours": [student.sleep_hours],
        "attendance_rate": [student.attendance_rate],
        "previous_score": [student.previous_score],
    })

    prediction = model.predict(input_data)

    return {
        "predicted_score": float(prediction[0])
    }