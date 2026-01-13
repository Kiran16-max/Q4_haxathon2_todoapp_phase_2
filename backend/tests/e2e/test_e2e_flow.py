# backend/tests/e2e/test_e2e_flow.py
import pytest
from fastapi.testclient import TestClient
from backend.main import app
from src.models.user import User
from src.models.task import Task
from src.database import engine
from sqlmodel import Session, select
from uuid import uuid4

@pytest.fixture
def client():
    """Create a test client for the API"""
    with TestClient(app) as test_client:
        yield test_client

def test_complete_application_flow(client):
    """Test the complete application flow: register, login, create task, update, delete"""
    
    # Generate unique email for test
    test_email = f"testuser_{uuid4()}@example.com"
    
    # 1. Register a new user
    register_response = client.post("/api/auth/register", json={
        "email": test_email,
        "name": "Test User",
        "password": "securepassword123"
    })
    
    assert register_response.status_code == 200
    register_data = register_response.json()
    assert "id" in register_data
    assert register_data["email"] == test_email
    
    # Extract the user ID from the response
    user_id = register_data["id"]
    
    # 2. Login with the new user
    login_response = client.post("/api/auth/login", json={
        "email": test_email,
        "password": "securepassword123"
    })
    
    assert login_response.status_code == 200
    login_data = login_response.json()
    assert "access_token" in login_data
    assert login_data["user"]["email"] == test_email
    
    # Extract the token for subsequent authenticated requests
    token = login_data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 3. Create a task
    task_response = client.post("/api/tasks", 
                              json={"title": "Test Task", "description": "Test Description"}, 
                              headers=headers)
    
    assert task_response.status_code == 201
    task_data = task_response.json()
    assert task_data["title"] == "Test Task"
    assert task_data["description"] == "Test Description"
    assert task_data["completed"] is False
    
    # Extract the task ID
    task_id = task_data["id"]
    
    # 4. Get all tasks (should include the one we just created)
    get_tasks_response = client.get("/api/tasks", headers=headers)
    assert get_tasks_response.status_code == 200
    tasks = get_tasks_response.json()
    assert len(tasks) >= 1
    task_titles = [task["title"] for task in tasks]
    assert "Test Task" in task_titles
    
    # 5. Update the task
    update_response = client.put(f"/api/tasks/{task_id}", 
                                json={"title": "Updated Test Task", "completed": True}, 
                                headers=headers)
    
    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task["title"] == "Updated Test Task"
    assert updated_task["completed"] is True
    
    # 6. Toggle task completion status
    toggle_response = client.patch(f"/api/tasks/{task_id}/complete", headers=headers)
    assert toggle_response.status_code == 200
    toggle_data = toggle_response.json()
    assert toggle_data["id"] == task_id
    assert toggle_data["completed"] is False  # Should be toggled back to False
    
    # 7. Delete the task
    delete_response = client.delete(f"/api/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 200
    
    # 8. Verify the task is deleted by trying to get it again
    get_single_task_response = client.get(f"/api/tasks/{task_id}", headers=headers)
    assert get_single_task_response.status_code == 404

if __name__ == "__main__":
    # Run the test with a temporary client
    with TestClient(app) as c:
        test_complete_application_flow(c)
        print("End-to-end test passed!")