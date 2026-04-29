# Student Score Prediction Web App

![CI](https://github.com/Kaan-YASSIBAS/student-score-prediction-api/actions/workflows/ci.yml/badge.svg)

A containerized Machine Learning web application built with **FastAPI**, **scikit-learn**, and a simple **HTML/CSS/JavaScript frontend**.  
The project predicts a student's exam score based on study habits and previous performance.

## Project Overview

This project demonstrates a basic end-to-end Machine Learning, API, frontend, containerization, testing, and CI workflow:

1. Create a small sample dataset
2. Train a Linear Regression model
3. Evaluate the model with basic regression metrics
4. Save the trained model with Joblib as a `.pkl` file
5. Load the saved model in a FastAPI backend
6. Validate incoming API requests with Pydantic
7. Expose health check and prediction endpoints
8. Build a simple frontend for user input and prediction display
9. Containerize backend and frontend with Docker
10. Run the full app with Docker Compose
11. Add container health checks
12. Test the backend API with Pytest
13. Run tests automatically with GitHub Actions CI

## Tech Stack

- Python
- FastAPI
- Pydantic
- scikit-learn
- pandas
- joblib
- Uvicorn
- HTML
- CSS
- JavaScript
- Nginx
- Docker
- Docker Compose
- Pytest
- GitHub Actions

## Project Structure

```text
student-score-prediction-api/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── model/
│   │       └── student_score_model.pkl
│   │
│   ├── scripts/
│   │   └── train_model.py
│   │
│   ├── tests/
│   │   └── test_api.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── pytest.ini
│   └── .dockerignore
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   ├── Dockerfile
│   └── .dockerignore
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Features

- Trains a Linear Regression model
- Saves the trained model as a `.pkl` file
- Serves the model with FastAPI
- Provides a simple frontend UI
- Accepts JSON input through the API
- Validates input values with Pydantic
- Returns predicted exam score as JSON
- Displays prediction result in the frontend
- Includes Swagger UI for testing the API
- Provides a `/health` endpoint
- Supports Docker containerization
- Supports Docker Compose with backend and frontend services
- Includes a container healthcheck using `/health`
- Includes backend API unit tests with Pytest
- Runs tests automatically with GitHub Actions CI

## Application Architecture

```text
Browser / Frontend UI
        ↓
POST /predict
        ↓
FastAPI Backend
        ↓
Pydantic Validation
        ↓
Pandas DataFrame
        ↓
Saved .pkl Linear Regression Model
        ↓
Prediction Response
```

## Services

| Service | Description | URL |
| --- | --- | --- |
| Frontend | HTML/CSS/JS user interface served by Nginx | `http://127.0.0.1:8080` |
| Backend API | FastAPI ML inference API | `http://127.0.0.1:8000` |
| Swagger UI | API documentation and testing UI | `http://127.0.0.1:8000/docs` |
| Health Check | Backend health endpoint | `http://127.0.0.1:8000/health` |

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

Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

## Train the Model

From the `backend` directory, run the training script:

```bash
python scripts/train_model.py
```

This will train the Linear Regression model and save it to:

```text
backend/app/model/student_score_model.pkl
```

## Run the Backend Locally

From the `backend` directory, start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend API will run at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Run the Full App with Docker Compose

From the project root directory, build and start both backend and frontend:

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

Stop the containers:

```bash
docker compose down
```

The app will be available at:

```text
Frontend:    http://127.0.0.1:8080
Backend API: http://127.0.0.1:8000
Swagger UI:  http://127.0.0.1:8000/docs
Health:      http://127.0.0.1:8000/health
```

The Docker Compose healthcheck uses:

```text
http://localhost:8000/health
```

## Run Backend Docker Image Manually

From the project root directory:

```bash
docker build -t student-score-api ./backend
```

Run the backend container:

```bash
docker run -p 8000:8000 student-score-api
```

The backend API will be available at:

```text
http://127.0.0.1:8000
```

## Run Frontend Docker Image Manually

From the project root directory:

```bash
docker build -t student-score-frontend ./frontend
```

Run the frontend container:

```bash
docker run -p 8080:80 student-score-frontend
```

The frontend will be available at:

```text
http://127.0.0.1:8080
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
The FastAPI backend loads this saved model and uses it to make predictions from incoming JSON requests.  
The frontend sends form data to the backend `/predict` endpoint and displays the predicted exam score.

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

This project uses `pytest` for backend API tests.

From the `backend` directory, run:

```bash
python -m pytest -v
```

The tests cover:

- Health check endpoint
- Successful prediction request
- Input validation errors
- Missing required fields

## Continuous Integration

This project uses GitHub Actions for CI.

The CI workflow runs automatically on:

- Pushes to the `main` branch
- Pull requests targeting the `main` branch

The workflow:

1. Checks out the repository
2. Sets up Python 3.12
3. Installs dependencies from `backend/requirements.txt`
4. Runs the Pytest test suite inside the `backend` directory

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
Data → Model Training → Model Saving → API Serving → Input Validation → Frontend UI → Testing → CI → Dockerization → Prediction
```

## Future Improvements

- Add a larger real-world dataset
- Add stronger input validation rules
- Add more unit and integration tests
- Add Kubernetes manifests
- Add monitoring and logging
- Deploy the application to a cloud platform
