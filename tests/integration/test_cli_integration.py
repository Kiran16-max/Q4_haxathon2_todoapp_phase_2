"""
Integration tests for the CLI interactions
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.cli.menu import add_task_ui, view_tasks_ui, update_task_ui, delete_task_ui, toggle_task_status_ui
from src.services.task_service import TaskService


class TestCLIIntegration(unittest.TestCase):
    
    def setUp(self):
        """Set up a fresh TaskService for each test."""
        self.task_service = TaskService()
    
    @patch('builtins.input')
    def test_add_task_ui_success(self, mock_input):
        """Test the add_task_ui function with valid inputs."""
        # Mock user inputs: title and description
        mock_input.side_effect = ["New Task", "This is a new task"]
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            add_task_ui(self.task_service)
        
        # Verify the task was added
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "New Task")
        self.assertEqual(tasks[0].description, "This is a new task")
        self.assertFalse(tasks[0].completed)
    
    @patch('builtins.input')
    def test_add_task_ui_empty_title(self, mock_input):
        """Test the add_task_ui function with empty title."""
        # Mock user inputs: empty title
        mock_input.side_effect = ["", "This is a description"]
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            add_task_ui(self.task_service)
        
        # Verify no task was added
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
        
        # Verify error message was printed
        output = captured_output.getvalue()
        self.assertIn("Error: Task title is required", output)
    
    @patch('builtins.input')
    def test_view_tasks_ui_empty(self, mock_input):
        """Test the view_tasks_ui function when no tasks exist."""
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            view_tasks_ui(self.task_service)
        
        # Verify appropriate message was printed
        output = captured_output.getvalue()
        self.assertIn("No tasks found", output)
    
    @patch('builtins.input')
    def test_view_tasks_ui_with_tasks(self, mock_input):
        """Test the view_tasks_ui function when tasks exist."""
        # Add a task first
        self.task_service.add_task("Test Task", "Test Description")
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            view_tasks_ui(self.task_service)
        
        # Verify task details were printed
        output = captured_output.getvalue()
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
    
    @patch('builtins.input')
    def test_update_task_ui_success(self, mock_input):
        """Test the update_task_ui function with valid inputs."""
        # Add a task first
        task_id = self.task_service.add_task("Original Title", "Original Description")
        
        # Mock user inputs: task ID, new title, new description
        mock_input.side_effect = [str(task_id), "Updated Title", "Updated Description"]
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            update_task_ui(self.task_service)
        
        # Verify the task was updated
        updated_task = self.task_service.get_task(task_id)
        self.assertEqual(updated_task.title, "Updated Title")
        self.assertEqual(updated_task.description, "Updated Description")
    
    @patch('builtins.input')
    def test_delete_task_ui_success(self, mock_input):
        """Test the delete_task_ui function with valid input."""
        # Add a task first
        task_id = self.task_service.add_task("Test Task", "Test Description")
        
        # Verify task exists
        self.assertEqual(len(self.task_service.get_all_tasks()), 1)
        
        # Mock user input: task ID to delete
        mock_input.side_effect = [str(task_id)]
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            delete_task_ui(self.task_service)
        
        # Verify the task was deleted
        self.assertEqual(len(self.task_service.get_all_tasks()), 0)
    
    @patch('builtins.input')
    def test_toggle_task_status_ui_success(self, mock_input):
        """Test the toggle_task_status_ui function with valid input."""
        # Add a task first
        task_id = self.task_service.add_task("Test Task", "Test Description")
        
        # Initially should be False
        initial_task = self.task_service.get_task(task_id)
        self.assertFalse(initial_task.completed)
        
        # Mock user input: task ID to toggle
        mock_input.side_effect = [str(task_id)]
        
        # Capture printed output
        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            toggle_task_status_ui(self.task_service)
        
        # Verify the task status was toggled
        toggled_task = self.task_service.get_task(task_id)
        self.assertTrue(toggled_task.completed)


if __name__ == '__main__':
    unittest.main()