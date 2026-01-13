# backend/tests/integration/test_auth_api.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture
def client():
    """Create a test client for the API"""
    with TestClient(app) as test_client:
        yield test_client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

# Additional tests would go here once we have a proper test database setup
# For now, we're just demonstrating the test structure

if __name__ == "__main__":
    # Simple demonstration
    with TestClient(app) as client:
        test_health_check(client)
        print("API integration test passed!")