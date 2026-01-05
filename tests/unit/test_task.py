"""
Unit tests for the Task model
"""

import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    
    def test_task_creation_valid(self):
        """Test creating a valid task."""
        task = Task(id=1, title="Test Task", description="Test Description", completed=False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
    
    def test_task_creation_defaults(self):
        """Test creating a task with default values."""
        task = Task(id=1, title="Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertIsNone(task.description)
        self.assertEqual(task.completed, False)
    
    def test_task_title_empty(self):
        """Test that creating a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(id=1, title="", description="Test Description")
    
    def test_task_title_whitespace_only(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            Task(id=1, title="   ", description="Test Description")
    
    def test_task_title_too_long(self):
        """Test that creating a task with title longer than 200 chars raises ValueError."""
        long_title = "A" * 201
        with self.assertRaises(ValueError):
            Task(id=1, title=long_title, description="Test Description")
    
    def test_task_description_too_long(self):
        """Test that creating a task with description longer than 1000 chars raises ValueError."""
        long_description = "A" * 1001
        with self.assertRaises(ValueError):
            Task(id=1, title="Test Task", description=long_description)
    
    def test_task_negative_id(self):
        """Test that creating a task with negative ID raises ValueError."""
        with self.assertRaises(ValueError):
            Task(id=-1, title="Test Task", description="Test Description")
    
    def test_task_zero_id(self):
        """Test that creating a task with zero ID raises ValueError."""
        with self.assertRaises(ValueError):
            Task(id=0, title="Test Task", description="Test Description")


if __name__ == '__main__':
    unittest.main()