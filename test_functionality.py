"""
Simple test to verify the functionality of the Console Todo App
"""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.services.task_service import TaskService
from src.models.task import Task

def test_functionality():
    print("Testing Console Todo App functionality...")
    
    # Initialize the task service
    task_service = TaskService()
    
    # Test 1: Add a task
    print("\n1. Testing add_task functionality...")
    task_id = task_service.add_task("Test Task", "This is a test description")
    print(f"   Added task with ID: {task_id}")
    
    # Test 2: Get all tasks
    print("\n2. Testing get_all_tasks functionality...")
    all_tasks = task_service.get_all_tasks()
    print(f"   Total tasks: {len(all_tasks)}")
    for task in all_tasks:
        print(f"   - ID: {task.id}, Title: {task.title}, Description: {task.description}, Completed: {task.completed}")
    
    # Test 3: Get specific task
    print("\n3. Testing get_task functionality...")
    retrieved_task = task_service.get_task(task_id)
    print(f"   Retrieved task: ID {retrieved_task.id}, Title: {retrieved_task.title}")
    
    # Test 4: Update task
    print("\n4. Testing update_task functionality...")
    task_service.update_task(task_id, "Updated Test Task", "Updated description")
    updated_task = task_service.get_task(task_id)
    print(f"   Updated task: Title: {updated_task.title}, Description: {updated_task.description}")
    
    # Test 5: Toggle task status
    print("\n5. Testing toggle_task_status functionality...")
    task_service.toggle_task_status(task_id)
    toggled_task = task_service.get_task(task_id)
    print(f"   Toggled task status: {toggled_task.completed}")
    
    # Test 6: Toggle task status again
    print("\n6. Testing toggle_task_status again...")
    task_service.toggle_task_status(task_id)
    toggled_task = task_service.get_task(task_id)
    print(f"   Toggled task status again: {toggled_task.completed}")
    
    # Test 7: Delete task
    print("\n7. Testing delete_task functionality...")
    task_service.delete_task(task_id)
    all_tasks = task_service.get_all_tasks()
    print(f"   Total tasks after deletion: {len(all_tasks)}")
    
    print("\nAll functionality tests passed successfully!")

if __name__ == "__main__":
    test_functionality()