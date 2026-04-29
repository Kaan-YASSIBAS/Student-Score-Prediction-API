# Student Score Prediction API

![CI](https://github.com/Kaan-YASSIBAS/student-score-prediction-api/actions/workflows/ci.yml/badge.svg)

A containerized Machine Learning inference API built with **FastAPI** and **scikit-learn**.  
The project predicts a student's exam score based on study habits and previous performance.

## Project Overview

This project demonstrates a basic end-to-end Machine Learning and API deployment workflow:

1. Create a small sample dataset
2. Train a Linear Regression model
3. Evaluate the model with basic regression metrics
4. Save the trained model with Joblib as a `.pkl` file
5. Load the saved model in a FastAPI application
6. Validate incoming API requests with Pydantic
7. Expose health check and prediction endpoints
8. Containerize the application with Docker
9. Run the API with Docker Compose and a container healthcheck
10. Test the API with Pytest
11. Run tests automatically with GitHub Actions CI

## Tech Stack

- Python
- FastAPI
- Pydantic
- scikit-learn
- pandas
- joblib
- Uvicorn
- Docker
- Docker Compose
- Pytest
- GitHub Actions

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
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── README.md
├── .dockerignore
└── .gitignore
```

## Features

- Trains a Linear Regression model
- Saves the trained model as a `.pkl` file
- Serves the model with FastAPI
- Accepts JSON input
- Validates input values with Pydantic
- Returns predicted exam score as JSON
- Includes Swagger UI for testing the API
- Provides a `/health` endpoint
- Supports Docker containerization
- Supports Docker Compose
- Includes a container healthcheck using `/health`
- Includes API unit tests with Pytest
- Runs tests automatically with GitHub Actions CI

## Input Features

The model uses the following features:

| Feature | Description |
| --- | --- |
| `hours_studied` | Number of hours the student studied |
| `sleep_hours` | Number of hours the student slept |
| `attendance_rate` | Student's attendance percentage |
| `previous_score` | Student's previous exam score |

## Input Validation

The API validates incoming request data using Pydantic.

Validation rules:

| Field | Rule |
| --- | --- |
| `hours_studied` | Must be between 0 and 24 |
| `sleep_hours` | Must be between 0 and 24 |
| `attendance_rate` | Must be between 0 and 100 |
| `previous_score` | Must be between 0 and 100 |

Invalid input returns a `422 Unprocessable Entity` response.

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

## Run the API Locally

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## Run with Docker

Build the Docker image:

```bash
docker build -t student-score-api .
```

Run the container:

```bash
docker run -p 8000:8000 student-score-api
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Run with Docker Compose

Build and start the API:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up --build -d
```

Check container status:

```bash
docker compose ps
```

Stop the container:

```bash
docker compose down
```

The Docker Compose healthcheck uses:

```text
http://localhost:8000/health
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

### Validation Error Example

Request body:

```json
{
  "hours_studied": -5,
  "sleep_hours": 30,
  "attendance_rate": 150,
  "previous_score": -10
}
```

Response status:

```text
422 Unprocessable Entity
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

## What Is a `.pkl` File?

A `.pkl` file is a serialized Python object file created with Pickle-compatible tools such as Joblib.

In this project, the `.pkl` file stores the trained `LinearRegression` model, including:

- The model type
- Learned coefficients
- Intercept value
- Internal scikit-learn model parameters

This allows the API to load the trained model and make predictions without retraining it every time.

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

## Running Tests

This project uses `pytest` for API tests.

Run tests locally:

```bash
python -m pytest -v
```

The tests cover:

- Health check endpoint
- Successful prediction request
- Input validation errors
- Missing required fields

Run tests inside Docker:

```bash
docker run --rm student-score-api pytest
```

## Continuous Integration

This project uses GitHub Actions for CI.

The CI workflow runs automatically on:

- Pushes to the `main` branch
- Pull requests targeting the `main` branch

The workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs dependencies from `requirements.txt`
4. Runs the Pytest test suite

Workflow file:

```text
.github/workflows/ci.yml
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
Data → Model Training → Model Saving → API Serving → Input Validation → Testing → CI → Dockerization → Prediction
```

## Future Improvements

- Add a larger real-world dataset
- Add stronger input validation rules
- Add more unit and integration tests
- Add Docker image build checks in CI
- Add Kubernetes manifests
- Add monitoring and logging
- Deploy the API to a cloud platform
