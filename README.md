# Student Score Prediction API

A simple Machine Learning API built with **FastAPI** and **scikit-learn**.  
The project predicts a student's exam score based on study habits and previous performance.

## Project Overview

This project demonstrates a basic end-to-end Machine Learning workflow:

1. Create a small dataset
2. Train a Linear Regression model
3. Save the trained model with Joblib
4. Load the saved model in a FastAPI application
5. Expose a prediction endpoint
6. Return the predicted exam score as JSON

## Tech Stack

- Python
- FastAPI
- scikit-learn
- pandas
- joblib
- Uvicorn

## Project Structure

```text
student-score-prediction-api/
│
├── app/
│   ├── main.py
│   └── model/
│       └── student_score_model.pkl
│
├── scripts/
│   └── train_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Features

- Trains a Linear Regression model
- Saves the trained model as a `.pkl` file
- Serves the model with FastAPI
- Accepts JSON input
- Returns predicted exam score
- Includes Swagger UI for testing the API

## Input Features

The model uses the following features:

| Feature | Description |
| --- | --- |
| `hours_studied` | Number of hours the student studied |
| `sleep_hours` | Number of hours the student slept |
| `attendance_rate` | Student's attendance percentage |
| `previous_score` | Student's previous exam score |

## Target

The model predicts:

| Target | Description |
| --- | --- |
| `exam_score` | Predicted exam score |

## Installation

Clone the repository:

```bash
git clone https://github.com/Kaan-YASSIBAS/student-score-prediction-api.git
cd student-score-prediction-api
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Train the Model

Run the training script:

```bash
python scripts/train_model.py
```

This will train the Linear Regression model and save it to:

```text
app/model/student_score_model.pkl
```

## Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "message": "Student Score Prediction API is running"
}
```

### Predict Student Score

```http
POST /predict
```

Request body:

```json
{
  "hours_studied": 7.5,
  "sleep_hours": 7,
  "attendance_rate": 90,
  "previous_score": 74
}
```

Response:

```json
{
  "predicted_score": 80.48837743174077
}
```

## How It Works

The model is trained using Linear Regression.

The general idea is:

```text
exam_score =
w1 * hours_studied +
w2 * sleep_hours +
w3 * attendance_rate +
w4 * previous_score +
bias
```

After training, the model is saved as a `.pkl` file using Joblib.  
The FastAPI application loads this saved model and uses it to make predictions from incoming JSON requests.

## Model Evaluation

The training script prints evaluation metrics such as:

```text
Mean Absolute Error
Mean Squared Error
```

Example output:

```text
Mean Absolute Error: 0.795
Mean Squared Error: 0.730
```

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 7.5,
    "sleep_hours": 7,
    "attendance_rate": 90,
    "previous_score": 74
  }'
```

## Notes

This project uses a small sample dataset for learning purposes.  
The goal is not to build a production-grade prediction model, but to understand the full workflow of:

```text
Data → Model Training → Model Saving → API Serving → Prediction
```

## Future Improvements

- Add a larger real-world dataset
- Add Docker support
- Add input validation rules
- Add unit tests
- Add CI/CD with GitHub Actions
- Deploy the API to a cloud platform
