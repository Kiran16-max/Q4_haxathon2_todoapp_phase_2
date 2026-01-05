# Quickstart Guide: Console Todo App

## Prerequisites
- Python 3.13+ installed on your system
- Basic command line knowledge

## Setup
1. Clone or download the repository
2. Navigate to the project directory in your terminal
3. Ensure Python 3.13+ is available by running `python --version`

## Running the Application
1. Navigate to the project root directory
2. Run the application with: `python src/cli/menu.py`
3. The main menu will appear with the following options:
   ```
   1. Add Task
   2. View Tasks
   3. Update Task
   4. Delete Task
   5. Mark Task Complete / Incomplete
   6. Exit
   ```

## Basic Usage
1. **Add Task**: Select option 1, enter a title (required) and description (optional)
2. **View Tasks**: Select option 2 to see all tasks with their status
3. **Update Task**: Select option 3, enter the task ID and new details
4. **Delete Task**: Select option 4, enter the task ID to remove
5. **Mark Complete/Incomplete**: Select option 5, enter the task ID to toggle status
6. **Exit**: Select option 6 to quit the application

## Example Workflow
1. Start the application
2. Add a task: "Buy groceries" with description "Milk, bread, eggs"
3. View tasks to confirm it was added
4. Mark the task as complete
5. Exit the application

## Troubleshooting
- If you get a "Python not found" error, ensure Python 3.13+ is installed and in your PATH
- If the application crashes, ensure all inputs are valid (e.g., numeric IDs when required)
- For empty title errors, ensure you provide a non-empty title when adding/updating tasks