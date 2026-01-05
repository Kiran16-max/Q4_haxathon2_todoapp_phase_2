"""
Task entity model for the Console Todo App.

This module defines the Task class that represents a single todo item
with id, title, description, and completion status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with id, title, description, and completion status.
    
    Attributes:
        id (int): Unique identifier for each task (positive integer, auto-generated)
        title (str): The main description of the task (required, non-empty, max 200 chars)
        description (str): Additional details about the task (optional, max 1000 chars)
        completed (bool): Track whether the task is completed (default: False)
    """
    
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
    def __post_init__(self):
        """Validate task attributes after initialization."""
        # Validate title
        if not self.title or not self.title.strip():
            raise ValueError("Task title must not be empty or null")
        
        if len(self.title.strip()) > 200:
            raise ValueError("Task title must be between 1 and 200 characters")
        
        # Validate description if provided
        if self.description and len(self.description) > 1000:
            raise ValueError("Task description, if provided, must be between 1 and 1000 characters")
        
        # Validate id
        if self.id <= 0:
            raise ValueError("Task id must be a positive integer")