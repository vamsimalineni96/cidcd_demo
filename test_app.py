from fastapi.testclient import TestClient
from cidcd_demo.app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.json() == {"result": 99}