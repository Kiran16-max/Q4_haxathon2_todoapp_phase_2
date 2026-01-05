"""
Main menu interface for the Console Todo App.

This module provides the console interface and menu handling for the application.
"""

import sys
import os
# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_service import TaskService
from src.lib.utils import get_valid_input, display_tasks


def main():
    """Main function to run the console todo app."""
    print("Welcome to the Console Todo App!")
    
    # Initialize the task service
    task_service = TaskService()
    
    # Main menu loop
    while True:
        print("\n--- Todo App Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete / Incomplete")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        try:
            if choice == "1":
                add_task_ui(task_service)
            elif choice == "2":
                view_tasks_ui(task_service)
            elif choice == "3":
                update_task_ui(task_service)
            elif choice == "4":
                delete_task_ui(task_service)
            elif choice == "5":
                toggle_task_status_ui(task_service)
            elif choice == "6":
                print("Thank you for using the Todo App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def add_task_ui(task_service: TaskService):
    """UI function to handle adding a new task."""
    print("\n--- Add New Task ---")
    
    title = input("Enter task title (required): ").strip()
    
    if not title:
        print("Error: Task title is required and cannot be empty.")
        return
    
    description_input = input("Enter task description (optional, press Enter to skip): ").strip()
    description = description_input if description_input else None
    
    try:
        task_id = task_service.add_task(title, description)
        print(f"Task added successfully with ID: {task_id}")
    except ValueError as e:
        print(f"Error adding task: {e}")


def view_tasks_ui(task_service: TaskService):
    """UI function to handle viewing all tasks."""
    print("\n--- View All Tasks ---")
    
    tasks = task_service.get_all_tasks()
    
    if not tasks:
        print("No tasks found. Your todo list is empty!")
        return
    
    display_tasks(tasks)


def update_task_ui(task_service: TaskService):
    """UI function to handle updating an existing task."""
    print("\n--- Update Task ---")
    
    try:
        task_id_input = input("Enter the task ID to update: ").strip()
        task_id = int(task_id_input)
        
        # Check if task exists
        task_service.get_task(task_id)
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return
    
    print(f"Current task details:")
    current_task = task_service.get_task(task_id)
    print(f"  ID: {current_task.id}")
    print(f"  Title: {current_task.title}")
    print(f"  Description: {current_task.description or 'None'}")
    print(f"  Status: {'Complete' if current_task.completed else 'Incomplete'}")
    
    new_title = input(f"Enter new title (or press Enter to keep '{current_task.title}'): ").strip()
    new_title = new_title if new_title else None
    
    new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
    new_description = new_description if new_description else None
    
    try:
        task_service.update_task(task_id, new_title, new_description)
        print("Task updated successfully!")
    except ValueError as e:
        print(f"Error updating task: {e}")


def delete_task_ui(task_service: TaskService):
    """UI function to handle deleting a task."""
    print("\n--- Delete Task ---")
    
    try:
        task_id_input = input("Enter the task ID to delete: ").strip()
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return
    
    try:
        task_service.delete_task(task_id)
        print(f"Task with ID {task_id} deleted successfully!")
    except ValueError as e:
        print(f"Error deleting task: {e}")


def toggle_task_status_ui(task_service: TaskService):
    """UI function to handle toggling task completion status."""
    print("\n--- Toggle Task Status ---")
    
    try:
        task_id_input = input("Enter the task ID to toggle status: ").strip()
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Please enter a valid task ID (number).")
        return
    
    try:
        task_service.toggle_task_status(task_id)
        task = task_service.get_task(task_id)
        status = "Complete" if task.completed else "Incomplete"
        print(f"Task status updated. Task is now {status}.")
    except ValueError as e:
        print(f"Error toggling task status: {e}")


if __name__ == "__main__":
    main()