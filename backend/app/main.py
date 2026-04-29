from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Student Score Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = Path(__file__).resolve().parent / "model" / "student_score_model.pkl"
model = joblib.load(MODEL_PATH)


class StudentInput(BaseModel):
    hours_studied: float = Field(
        ...,
        ge=0,
        le=24,
        description="Number of hours the student studied. Must be between 0 and 24."
    )

    sleep_hours: float = Field(
        ...,
        ge=0,
        le=24,
        description="Number of hours the student slept. Must be between 0 and 24."
    )

    attendance_rate: float = Field(
        ...,
        ge=0,
        le=100,
        description="Student attendance percentage. Must be between 0 and 100."
    )

    previous_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Student's previous exam score. Must be between 0 and 100."
    )


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