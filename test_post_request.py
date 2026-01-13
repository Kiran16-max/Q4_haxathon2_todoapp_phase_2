import requests
import json

# This script tests the POST /api/tasks endpoint to ensure it works with the correct Authorization header format

# First, we need to register a user to get an access token
register_url = "http://localhost:8000/api/auth/register"
register_payload = {
    "email": "test@example.com",
    "name": "Test User",
    "password": "testpassword123"
}

print("Registering user...")
register_response = requests.post(register_url, json=register_payload)
if register_response.status_code == 200:
    print("User registered successfully")
    response_data = register_response.json()
    access_token = response_data.get("access_token")
    print(f"Access token received: {access_token[:20]}...")  # Show first 20 chars only
else:
    print(f"Registration failed with status code: {register_response.status_code}")
    print(f"Response: {register_response.text}")
    exit(1)

# Now make the POST request to /api/tasks with the correct Authorization header
tasks_url = "http://localhost:8000/api/tasks"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

task_payload = {
    "title": "Test Task",
    "description": "This is a test task created via API"
}

print("\nMaking POST request to /api/tasks...")
response = requests.post(tasks_url, headers=headers, json=task_payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200 or response.status_code == 201:
    print("\n✅ SUCCESS: POST /api/tasks request completed with 200/201 OK")
else:
    print(f"\n❌ FAILED: POST /api/tasks request failed with status code {response.status_code}")