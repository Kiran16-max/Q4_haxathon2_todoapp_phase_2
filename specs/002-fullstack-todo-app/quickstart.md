# Quickstart Guide: Full-Stack Todo Web Application with AI Chatbot

## Prerequisites
- Node.js 18+ installed on your system
- Python 3.11+ installed on your system
- PostgreSQL (local or cloud instance)
- OpenAI API key
- Basic command line knowledge

## Setup
1. Clone or download the repository
2. Navigate to the project directory in your terminal
3. Install frontend dependencies: `cd frontend && npm install`
4. Install backend dependencies: `cd backend && pip install -r requirements.txt`
5. Set up environment variables (see Environment Variables section below)

## Running the Application Locally
1. Start the backend server:
   - Navigate to the backend directory: `cd backend`
   - Run: `uvicorn main:app --reload`
   - The API will be available at `http://localhost:8000`

2. Start the frontend development server:
   - Navigate to the frontend directory: `cd frontend`
   - Run: `npm run dev`
   - The application will be available at `http://localhost:3000`

## Environment Variables
Create `.env` files in both frontend and backend directories:

**Frontend (.env.local):**
```
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
```

**Backend (.env):**
```
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app_db
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_jwt_secret_key_here
```

## Basic Usage
1. **Register/Login**: Visit the homepage and click "Sign Up" to create an account, or "Log In" if you already have one
2. **Dashboard**: After login, you'll be taken to the dashboard where you can see all your tasks
3. **Add Task**: Click "Add Task" button to create a new task with title and description
4. **Manage Tasks**: Update, delete, or mark tasks as complete/incomplete using the task card controls
5. **AI Chatbot**: Use the chat interface to manage tasks with natural language commands like "Add a task to buy groceries"
6. **Filter Tasks**: Use the filter controls to view all, pending, or completed tasks

## Example Workflow
1. Register a new account
2. Log in to the dashboard
3. Add a task: "Buy groceries" with description "Milk, bread, eggs"
4. View tasks to confirm it was added
5. Mark the task as complete
6. Interact with the AI chatbot to add another task: "Schedule dentist appointment"
7. Logout and log back in to verify data persistence

## API Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get a specific task
- `PUT /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task
- `PATCH /api/tasks/{id}/complete` - Toggle task completion status
- `POST /api/chat` - AI chatbot endpoint

## Troubleshooting
- If you get a "Database connection failed" error, ensure PostgreSQL is running and credentials are correct
- If the AI chatbot isn't responding, check that your OpenAI API key is valid and has sufficient credits
- If authentication isn't working, ensure the JWT secret key is properly configured
- For UI styling issues, verify Tailwind CSS is properly configured in the frontend