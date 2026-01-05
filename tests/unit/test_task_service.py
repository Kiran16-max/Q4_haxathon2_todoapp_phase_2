"""
Unit tests for the TaskService
"""

import unittest
from src.services.task_service import TaskService
from src.models.task import Task


class TestTaskService(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh TaskService for each test."""
        self.service = TaskService()
    
    def test_add_task_success(self):
        """Test adding a task successfully."""
        task_id = self.service.add_task("Test Task", "Test Description")
        self.assertEqual(task_id, 1)
        
        # Verify the task was added
        task = self.service.get_task(task_id)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
    
    def test_add_task_without_description(self):
        """Test adding a task without description."""
        task_id = self.service.add_task("Test Task")
        task = self.service.get_task(task_id)
        self.assertEqual(task.title, "Test Task")
        self.assertIsNone(task.description)
    
    def test_add_task_empty_title(self):
        """Test that adding a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.add_task("", "Test Description")
    
    def test_add_task_whitespace_title(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.add_task("   ", "Test Description")
    
    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist."""
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
    
    def test_get_all_tasks_with_tasks(self):
        """Test getting all tasks when some exist."""
        self.service.add_task("Task 1", "Description 1")
        self.service.add_task("Task 2", "Description 2")
        
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        
        titles = [task.title for task in tasks]
        self.assertIn("Task 1", titles)
        self.assertIn("Task 2", titles)
    
    def test_get_task_success(self):
        """Test getting a specific task."""
        task_id = self.service.add_task("Test Task", "Test Description")
        task = self.service.get_task(task_id)
        
        self.assertEqual(task.id, task_id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
    
    def test_get_task_not_found(self):
        """Test that getting a non-existent task raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.get_task(999)
    
    def test_update_task_title(self):
        """Test updating a task's title."""
        task_id = self.service.add_task("Original Title", "Original Description")
        
        result = self.service.update_task(task_id, "New Title")
        self.assertTrue(result)
        
        updated_task = self.service.get_task(task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "Original Description")
    
    def test_update_task_description(self):
        """Test updating a task's description."""
        task_id = self.service.add_task("Original Title", "Original Description")
        
        result = self.service.update_task(task_id, description="New Description")
        self.assertTrue(result)
        
        updated_task = self.service.get_task(task_id)
        self.assertEqual(updated_task.title, "Original Title")
        self.assertEqual(updated_task.description, "New Description")
    
    def test_update_task_both_fields(self):
        """Test updating both title and description."""
        task_id = self.service.add_task("Original Title", "Original Description")
        
        result = self.service.update_task(task_id, "New Title", "New Description")
        self.assertTrue(result)
        
        updated_task = self.service.get_task(task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")
    
    def test_update_task_not_found(self):
        """Test that updating a non-existent task raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.update_task(999, "New Title")
    
    def test_update_task_empty_title(self):
        """Test that updating with empty title raises ValueError."""
        task_id = self.service.add_task("Original Title", "Original Description")
        
        with self.assertRaises(ValueError):
            self.service.update_task(task_id, "")
    
    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        task_id = self.service.add_task("Test Task", "Test Description")
        
        result = self.service.delete_task(task_id)
        self.assertTrue(result)
        
        # Verify the task no longer exists
        with self.assertRaises(ValueError):
            self.service.get_task(task_id)
    
    def test_delete_task_not_found(self):
        """Test that deleting a non-existent task raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.delete_task(999)
    
    def test_toggle_task_status(self):
        """Test toggling a task's completion status."""
        task_id = self.service.add_task("Test Task", "Test Description")
        
        # Initially should be False
        task = self.service.get_task(task_id)
        self.assertFalse(task.completed)
        
        # Toggle to True
        result = self.service.toggle_task_status(task_id)
        self.assertTrue(result)
        
        task = self.service.get_task(task_id)
        self.assertTrue(task.completed)
        
        # Toggle back to False
        result = self.service.toggle_task_status(task_id)
        self.assertTrue(result)
        
        task = self.service.get_task(task_id)
        self.assertFalse(task.completed)
    
    def test_toggle_task_status_not_found(self):
        """Test that toggling a non-existent task raises ValueError."""
        with self.assertRaises(ValueError):
            self.service.toggle_task_status(999)


if __name__ == '__main__':
    unittest.main()