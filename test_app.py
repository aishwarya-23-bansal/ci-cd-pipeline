
from app import app


def test_homepage():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Automated CI/CD Pipeline" in response.data


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["version"] == "3.0"
