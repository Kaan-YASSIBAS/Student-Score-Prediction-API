from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Student Score Prediction API is running"
    }


def test_predict_score_success():
    payload = {
        "hours_studied": 7.5,
        "sleep_hours": 7,
        "attendance_rate": 90,
        "previous_score": 74
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "predicted_score" in data
    assert isinstance(data["predicted_score"], float)
    assert data["predicted_score"] > 0


def test_predict_score_invalid_negative_hours():
    payload = {
        "hours_studied": -5,
        "sleep_hours": 7,
        "attendance_rate": 90,
        "previous_score": 74
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_score_invalid_attendance_rate():
    payload = {
        "hours_studied": 7.5,
        "sleep_hours": 7,
        "attendance_rate": 150,
        "previous_score": 74
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_score_missing_field():
    payload = {
        "hours_studied": 7.5,
        "sleep_hours": 7,
        "attendance_rate": 90
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 422