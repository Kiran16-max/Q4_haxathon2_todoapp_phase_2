"""
Utility functions for the Console Todo App.

This module provides utility functions for input validation and formatting.
"""

from typing import List
from src.models.task import Task


def get_valid_input(prompt: str, validator_func=None):
    """
    Get valid input from the user with optional validation.
    
    Args:
        prompt (str): The prompt to display to the user
        validator_func (callable, optional): Function to validate the input
        
    Returns:
        str: The validated user input
    """
    while True:
        user_input = input(prompt).strip()
        
        if validator_func:
            if validator_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")
        else:
            return user_input


def display_tasks(tasks: List[Task]):
    """
    Display a list of tasks in a formatted way.
    
    Args:
        tasks (List[Task]): List of task objects to display
    """
    print("\nYour Tasks:")
    print("-" * 60)
    
    for task in tasks:
        status = "✔ Complete" if task.completed else "❌ Incomplete"
        description = task.description if task.description else "No description"
        
        print(f"ID: {task.id}")
        print(f"Title: {task.title}")
        print(f"Description: {description}")
        print(f"Status: {status}")
        print("-" * 60)


def validate_task_title(title: str) -> bool:
    """
    Validate a task title according to the requirements.
    
    Args:
        title (str): The title to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not title or not title.strip():
        return False
    
    if len(title.strip()) > 200:
        return False
    
    return True


def validate_task_description(description: str) -> bool:
    """
    Validate a task description according to the requirements.
    
    Args:
        description (str): The description to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not description:
        return True  # Description is optional
    
    if len(description) > 1000:
        return False
    
    return True