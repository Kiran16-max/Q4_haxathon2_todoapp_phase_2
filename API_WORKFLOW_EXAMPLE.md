# Todo App API Full Workflow Example

This document provides a comprehensive guide to using the Todo App API with JWT authentication and SQLModel. It demonstrates the complete workflow from user registration to task management.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [API Endpoints](#api-endpoints)
3. [Complete Workflow Example](#complete-workflow-example)
4. [cURL Examples](#curl-examples)
5. [Python Requests Examples](#python-requests-examples)
6. [Error Handling](#error-handling)
7. [Response Status Codes](#response-status-codes)

## Prerequisites

- Backend server running on `http://localhost:8000`
- Python 3.8+ with required packages installed
- Understanding of JWT authentication

## API Endpoints

### Authentication Endpoints
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Authenticate user and get JWT token

### Task Management Endpoints
- `GET /api/tasks` - Get all tasks for the authenticated user
- `POST /api/tasks` - Create a new task for the authenticated user
- `GET /api/tasks/{task_id}` - Get a specific task for the authenticated user
- `PUT /api/tasks/{task_id}` - Update a specific task for the authenticated user
- `DELETE /api/tasks/{task_id}` - Delete a specific task for the authenticated user
- `PATCH /api/tasks/{task_id}/complete` - Toggle completion status of a task

## Complete Workflow Example

### Step 1: User Registration

**Request:**
```
POST /api/auth/register
Content-Type: application/json

{
  "email": "testuser@example.com",
  "name": "Test User",
  "password": "123456"
}
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "testuser@example.com",
    "name": "Test User"
  }
}
```

### Step 2: User Login

**Request:**
```
POST /api/auth/login
Content-Type: application/x-www-form-urlencoded

username=testuser@example.com&password=123456
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "testuser@example.com",
    "name": "Test User"
  }
}
```

### Step 3: Using JWT Token for Authentication

For all subsequent requests to task endpoints, include the JWT token in the Authorization header:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Step 4: Create a New Task

**Request:**
```
POST /api/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "Test Task",
  "description": "This is a test task",
  "completed": false
}
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "title": "Test Task",
  "description": "This is a test task",
  "completed": false,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "created_at": "2023-01-01T12:00:00",
  "updated_at": "2023-01-01T12:00:00"
}
```

### Step 5: Read All Tasks

**Request:**
```
GET /api/tasks
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

[
  {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "title": "Test Task",
    "description": "This is a test task",
    "completed": false,
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "created_at": "2023-01-01T12:00:00",
    "updated_at": "2023-01-01T12:00:00"
  }
]
```

### Step 6: Update a Task

**Request:**
```
PUT /api/tasks/f47ac10b-58cc-4372-a567-0e02b2c3d479
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "title": "Updated Test Task",
  "description": "This is an updated test task",
  "completed": true
}
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "title": "Updated Test Task",
  "description": "This is an updated test task",
  "completed": true,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "created_at": "2023-01-01T12:00:00",
  "updated_at": "2023-01-01T13:00:00"
}
```

### Step 7: Toggle Task Completion

**Request:**
```
PATCH /api/tasks/f47ac10b-58cc-4372-a567-0e02b2c3d479/complete
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "completed": false
}
```

### Step 8: Delete a Task

**Request:**
```
DELETE /api/tasks/f47ac10b-58cc-4372-a567-0e02b2c3d479
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Successful Response:**
```
Status: 200 OK
Content-Type: application/json

{
  "message": "Task deleted successfully"
}
```

## cURL Examples

### Register a User
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "testuser@example.com",
    "name": "Test User",
    "password": "123456"
  }'
```

### Login
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'username=testuser@example.com&password=123456'
```

### Create a Task (with JWT token)
```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Task",
    "description": "This is a test task"
  }'
```

### Get All Tasks
```bash
curl -X GET http://localhost:8000/api/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

### Update a Task
```bash
curl -X PUT http://localhost:8000/api/tasks/TASK_ID_HERE \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Test Task",
    "completed": true
  }'
```

### Toggle Task Completion
```bash
curl -X PATCH http://localhost:8000/api/tasks/TASK_ID_HERE/complete \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

### Delete a Task
```bash
curl -X DELETE http://localhost:8000/api/tasks/TASK_ID_HERE \
  -H "Authorization: Bearer YOUR_JWT_TOKEN_HERE"
```

## Python Requests Examples

### Register a User
```python
import requests

url = "http://localhost:8000/api/auth/register"
payload = {
    "email": "testuser@example.com",
    "name": "Test User",
    "password": "123456"
}

response = requests.post(url, json=payload)
if response.status_code == 200:
    data = response.json()
    token = data["access_token"]
    print(f"Registration successful. Token: {token}")
else:
    print(f"Registration failed: {response.status_code} - {response.text}")
```

### Login
```python
import requests

url = "http://localhost:8000/api/auth/login"
data = {
    "username": "testuser@example.com",
    "password": "123456"
}

response = requests.post(url, data=data)
if response.status_code == 200:
    data = response.json()
    token = data["access_token"]
    print(f"Login successful. Token: {token}")
else:
    print(f"Login failed: {response.status_code} - {response.text}")
```

### Create a Task
```python
import requests

url = "http://localhost:8000/api/tasks"
headers = {
    "Authorization": f"Bearer YOUR_JWT_TOKEN_HERE",
    "Content-Type": "application/json"
}
payload = {
    "title": "Test Task",
    "description": "This is a test task"
}

response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
    task = response.json()
    print(f"Task created: {task['id']}")
else:
    print(f"Task creation failed: {response.status_code} - {response.text}")
```

### Get All Tasks
```python
import requests

url = "http://localhost:8000/api/tasks"
headers = {
    "Authorization": f"Bearer YOUR_JWT_TOKEN_HERE"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    tasks = response.json()
    print(f"Retrieved {len(tasks)} tasks")
    for task in tasks:
        print(f"- {task['title']} ({'✓' if task['completed'] else '○'})")
else:
    print(f"Getting tasks failed: {response.status_code} - {response.text}")
```

### Update a Task
```python
import requests

task_id = "TASK_ID_HERE"
url = f"http://localhost:8000/api/tasks/{task_id}"
headers = {
    "Authorization": f"Bearer YOUR_JWT_TOKEN_HERE",
    "Content-Type": "application/json"
}
payload = {
    "title": "Updated Test Task",
    "completed": True
}

response = requests.put(url, headers=headers, json=payload)
if response.status_code == 200:
    task = response.json()
    print(f"Task updated: {task['title']}")
else:
    print(f"Task update failed: {response.status_code} - {response.text}")
```

### Toggle Task Completion
```python
import requests

task_id = "TASK_ID_HERE"
url = f"http://localhost:8000/api/tasks/{task_id}/complete"
headers = {
    "Authorization": f"Bearer YOUR_JWT_TOKEN_HERE"
}

response = requests.patch(url, headers=headers)
if response.status_code == 200:
    result = response.json()
    status = "completed" if result["completed"] else "not completed"
    print(f"Task {result['id']} is now {status}")
else:
    print(f"Toggle completion failed: {response.status_code} - {response.text}")
```

### Delete a Task
```python
import requests

task_id = "TASK_ID_HERE"
url = f"http://localhost:8000/api/tasks/{task_id}"
headers = {
    "Authorization": f"Bearer YOUR_JWT_TOKEN_HERE"
}

response = requests.delete(url, headers=headers)
if response.status_code == 200:
    print("Task deleted successfully")
else:
    print(f"Task deletion failed: {response.status_code} - {response.text}")
```

## Error Handling

The API implements comprehensive error handling with appropriate HTTP status codes:

- **400 Bad Request**: Invalid request format or validation errors
- **401 Unauthorized**: Invalid or missing JWT token
- **404 Not Found**: Resource not found (e.g., task doesn't exist)
- **409 Conflict**: Resource already exists (e.g., email already registered)
- **500 Internal Server Error**: Unexpected server errors

### Example Error Response
```json
{
  "detail": "Task not found"
}
```

## Response Status Codes

| Endpoint | Successful Status | Error Status |
|----------|------------------|--------------|
| POST /api/auth/register | 200 | 409, 500 |
| POST /api/auth/login | 200 | 401, 500 |
| GET /api/tasks | 200 | 401, 500 |
| POST /api/tasks | 200 | 401, 500 |
| GET /api/tasks/{id} | 200 | 401, 404, 500 |
| PUT /api/tasks/{id} | 200 | 401, 404, 500 |
| PATCH /api/tasks/{id}/complete | 200 | 401, 404, 500 |
| DELETE /api/tasks/{id} | 200 | 401, 404, 500 |

## Security Features

- JWT tokens with configurable expiration (default: 30 minutes)
- Password hashing using bcrypt with 12 rounds
- SQL injection protection through SQLModel
- Proper authentication and authorization checks
- Rate limiting considerations (implementation may vary)
- Secure password storage with salted hashes
- Access control to ensure users can only access their own tasks

## Production Considerations

- Use HTTPS in production environments
- Store JWT secret in environment variables
- Implement proper rate limiting
- Add request validation and sanitization
- Monitor and log security events
- Regular security audits and updates
- Backup and recovery procedures