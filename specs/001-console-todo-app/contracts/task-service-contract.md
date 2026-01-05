# Internal API Contracts: Console Todo App

## Task Service Interface

### add_task(title: str, description: str = None) -> int
- **Purpose**: Creates a new task with the given title and optional description
- **Input**: 
  - title (str): Required task title (non-empty)
  - description (str, optional): Optional task description
- **Output**: int - The ID of the newly created task
- **Errors**: ValueError if title is empty

### get_all_tasks() -> List[dict]
- **Purpose**: Retrieves all tasks in the system
- **Input**: None
- **Output**: List of task dictionaries with id, title, description, and completed status
- **Errors**: None

### get_task(task_id: int) -> dict
- **Purpose**: Retrieves a specific task by its ID
- **Input**: task_id (int): The ID of the task to retrieve
- **Output**: Task dictionary with id, title, description, and completed status
- **Errors**: ValueError if task_id does not exist

### update_task(task_id: int, title: str = None, description: str = None) -> bool
- **Purpose**: Updates an existing task with new information
- **Input**: 
  - task_id (int): The ID of the task to update
  - title (str, optional): New title if provided
  - description (str, optional): New description if provided
- **Output**: bool - True if update was successful, False otherwise
- **Errors**: ValueError if task_id does not exist

### delete_task(task_id: int) -> bool
- **Purpose**: Removes a task from the system
- **Input**: task_id (int): The ID of the task to delete
- **Output**: bool - True if deletion was successful, False otherwise
- **Errors**: ValueError if task_id does not exist

### toggle_task_status(task_id: int) -> bool
- **Purpose**: Toggles the completion status of a task
- **Input**: task_id (int): The ID of the task to toggle
- **Output**: bool - True if toggle was successful, False otherwise
- **Errors**: ValueError if task_id does not exist