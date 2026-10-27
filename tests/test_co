from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["system"] == "SB-61-Core"
    assert response.json()["status"] == "Operational"

def test_secure_status_unauthorized():
    response = client.get("/secure-status")
    assert response.status_code == 403

def test_secure_status_authorized():
    headers = {"X-Neural-Token": "SB61-SECURE-NEURAL-KEY-2026"}
    response = client.get("/secure-status", headers=headers)
    assert response.status_code == 200
    assert response.json()["authorization"] == "Granted"

def test_process_neural_signal():
    headers = {"X-Neural-Token": "SB61-SECURE-NEURAL-KEY-2026"}
    payload = {"data_signal": "Unit Test Pulse"}
    response = client.post("/process", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["processed_status"] == "Success"

