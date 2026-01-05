# Console Todo App

A simple, menu-driven todo application that runs in the console with in-memory storage.

## Features

- Add new tasks with titles and optional descriptions
- View all tasks with their completion status
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Menu-driven interface

## Prerequisites

- Python 3.13+ installed on your system

## Setup

1. Clone or download this repository
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

## Architecture

The application follows a clear separation of concerns:

- **Models** (`src/models/`): Data structures (Task entity)
- **Services** (`src/services/`): Business logic (TaskService)
- **CLI** (`src/cli/`): User interface (menu system)
- **Lib** (`src/lib/`): Utility functions

## Data Model

Each task contains:
- `id`: Unique integer identifier
- `title`: Required string (non-empty)
- `description`: Optional string
- `completed`: Boolean status (default: False)

## Error Handling

The application handles invalid inputs gracefully:
- Empty titles are rejected
- Invalid task IDs are handled with appropriate messages
- Non-numeric inputs where numbers are expected are caught
- The application will not crash on invalid inputs