# backend/tests/unit/test_models.py
import pytest
from uuid import uuid4
from src.models.user import User
from src.models.task import Task

def test_user_model():
    """Test the User model creation and properties"""
    user_data = {
        "id": uuid4(),
        "email": "test@example.com",
        "name": "Test User",
        "password_hash": "hashed_password_here",
    }
    
    user = User(
        id=user_data["id"],
        email=user_data["email"],
        name=user_data["name"],
        password_hash=user_data["password_hash"]
    )
    
    assert user.email == user_data["email"]
    assert user.name == user_data["name"]
    assert user.password_hash == user_data["password_hash"]
    assert user.id == user_data["id"]


def test_task_model():
    """Test the Task model creation and properties"""
    from uuid import uuid4
    
    user_id = uuid4()
    task_data = {
        "id": uuid4(),
        "user_id": user_id,
        "title": "Test Task",
        "description": "Test Description",
        "completed": False
    }
    
    task = Task(
        id=task_data["id"],
        user_id=task_data["user_id"],
        title=task_data["title"],
        description=task_data["description"],
        completed=task_data["completed"]
    )
    
    assert task.title == task_data["title"]
    assert task.description == task_data["description"]
    assert task.completed == task_data["completed"]
    assert task.user_id == user_id
    assert task.id == task_data["id"]


if __name__ == "__main__":
    test_user_model()
    test_task_model()
    print("All model tests passed!")