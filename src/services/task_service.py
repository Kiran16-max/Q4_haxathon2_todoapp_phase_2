"""
Task service for the Console Todo App.

This module provides business logic for task operations including
creating, reading, updating, and deleting tasks with in-memory storage.
"""

from typing import Dict, List, Optional
from src.models.task import Task


class TaskService:
    """
    Provides business logic for task operations with in-memory storage.
    
    The service handles all CRUD operations for tasks using a dictionary
    for storage with ID as key and Task object as value.
    """
    
    def __init__(self):
        """Initialize the task service with an empty storage dictionary and ID counter."""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> int:
        """
        Creates a new task with the given title and optional description.
        
        Args:
            title (str): Required task title (non-empty)
            description (str, optional): Optional task description
            
        Returns:
            int: The ID of the newly created task
            
        Raises:
            ValueError: If title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title must not be empty or null")
        
        # Create a new task with the next available ID
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            completed=False
        )
        
        # Add task to storage
        self._tasks[self._next_id] = task
        
        # Increment the ID counter for the next task
        task_id = self._next_id
        self._next_id += 1
        
        return task_id
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieves all tasks in the system.
        
        Returns:
            List[Task]: List of all task objects
        """
        return list(self._tasks.values())
    
    def get_task(self, task_id: int) -> Task:
        """
        Retrieves a specific task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve
            
        Returns:
            Task: Task object with id, title, description, and completed status
            
        Raises:
            ValueError: If task_id does not exist
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        return self._tasks[task_id]
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates an existing task with new information.
        
        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title if provided
            description (str, optional): New description if provided
            
        Returns:
            bool: True if update was successful, False otherwise
            
        Raises:
            ValueError: If task_id does not exist
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        task = self._tasks[task_id]
        
        # Update title if provided
        if title is not None:
            if not title.strip():
                raise ValueError("Task title must not be empty or null")
            task.title = title.strip()
        
        # Update description if provided
        if description is not None:
            task.description = description.strip() if description else None
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Removes a task from the system.
        
        Args:
            task_id (int): The ID of the task to delete
            
        Returns:
            bool: True if deletion was successful, False otherwise
            
        Raises:
            ValueError: If task_id does not exist
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        del self._tasks[task_id]
        return True
    
    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggles the completion status of a task.
        
        Args:
            task_id (int): The ID of the task to toggle
            
        Returns:
            bool: True if toggle was successful, False otherwise
            
        Raises:
            ValueError: If task_id does not exist
        """
        if task_id not in self._tasks:
            raise ValueError(f"Task with ID {task_id} does not exist")
        
        task = self._tasks[task_id]
        task.completed = not task.completed
        return True