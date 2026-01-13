# Full-Stack Todo Web Application with AI Chatbot

A production-ready, multi-user todo application with authentication, persistent storage, modern UI/UX, and AI chatbot integration.

## Features

- **User Authentication**: Secure registration and login with JWT tokens
- **Task Management**: Full CRUD operations for managing tasks
- **Modern UI/UX**: Responsive design with dark/light mode support
- **AI Chatbot**: Natural language processing for task management
- **Multi-User Support**: Each user has isolated data and tasks
- **Security**: Implements security best practices with CORS, security headers, and input validation
- **Scalability**: Designed for horizontal scaling with stateless architecture

## Tech Stack

### Frontend
- Next.js 16
- TypeScript 5
- Tailwind CSS
- React 19

### Backend
- FastAPI
- Python 3.11+
- SQLModel
- Neon PostgreSQL
- OpenAI API

## Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL (local or cloud instance)
- OpenAI API key

## Setup

1. Clone the repository
2. Install frontend dependencies: `cd frontend && npm install`
3. Install backend dependencies: `cd backend && pip install -r requirements.txt`
4. Set up environment variables (see Environment Variables section below)

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

## Running the Application

### Backend
1. Navigate to the backend directory: `cd backend`
2. Run: `uvicorn main:app --reload`
3. The API will be available at `http://localhost:8000`

### Frontend
1. Navigate to the frontend directory: `cd frontend`
2. Run: `npm run dev`
3. The application will be available at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login

### Task Management
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get a specific task
- `PUT /api/tasks/{id}` - Update a task
- `DELETE /api/tasks/{id}` - Delete a task
- `PATCH /api/tasks/{id}/complete` - Toggle task completion status

### AI Chatbot
- `POST /api/chat` - AI chatbot endpoint

## Architecture

The application follows a clear separation of concerns:

- **Frontend**: Next.js application handling UI/UX and user interactions
- **Backend**: FastAPI application managing business logic, data persistence, and AI integration
- **Database**: Neon PostgreSQL for persistent data storage
- **AI**: OpenAI API for natural language processing

## Security Features

- JWT-based authentication with secure token handling
- CORS policy configured for secure cross-origin requests
- Security headers implemented (X-Content-Type-Options, X-Frame-Options, etc.)
- Input validation and sanitization
- SQL injection prevention through SQLModel ORM
- Rate limiting (implementable via middleware)

## Testing

The application includes comprehensive testing at multiple levels:

- **Unit Tests**: For individual components and functions
- **Integration Tests**: For API endpoints and database interactions
- **Component Tests**: For frontend UI components

To run tests:
- Backend: `cd backend && pytest`
- Frontend: `cd frontend && npm test`

## Deployment

The application is designed for containerized deployment:

1. Build the frontend: `cd frontend && npm run build`
2. Containerize with Docker using the provided Dockerfile
3. Deploy to your preferred cloud platform (AWS, GCP, Azure, etc.)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.