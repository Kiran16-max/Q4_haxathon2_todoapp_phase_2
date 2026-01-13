# Data Model: Full-Stack Todo Web Application with AI Chatbot

## User Entity

### Attributes
- **id**: UUID (primary key)
  - Purpose: Unique identifier for each user
  - Constraints: Auto-generated UUID, not null, unique
- **email**: String (required, unique)
  - Purpose: User's email address for login
  - Constraints: Required field, unique, valid email format, max length 255 characters
- **name**: String (optional)
  - Purpose: User's display name
  - Constraints: Optional field, max length 255 characters
- **password_hash**: String (required)
  - Purpose: Hashed password for authentication
  - Constraints: Required field, securely hashed
- **created_at**: DateTime (default: now)
  - Purpose: Timestamp of user creation
  - Constraints: Auto-generated on creation
- **updated_at**: DateTime (default: now)
  - Purpose: Timestamp of last update
  - Constraints: Auto-generated on update

### Validation Rules
1. **Email Required**: User.email must not be empty or null
2. **Email Format**: User.email must be a valid email address
3. **Email Uniqueness**: Each User.email must be unique within the system
4. **Password Strength**: User.password must meet minimum security requirements

## Task Entity

### Attributes
- **id**: UUID (primary key)
  - Purpose: Unique identifier for each task
  - Constraints: Auto-generated UUID, not null, unique
- **user_id**: UUID (foreign key to User.id, required)
  - Purpose: Links task to the owning user
  - Constraints: References User.id, cascading delete
- **title**: String (required)
  - Purpose: The main description of the task
  - Constraints: Required field, non-empty, max length 200 characters
- **description**: String (optional)
  - Purpose: Additional details about the task
  - Constraints: Optional field, max length 1000 characters
- **completed**: Boolean (default: False)
  - Purpose: Track whether the task is completed
  - Constraints: Boolean value, defaults to False
- **created_at**: DateTime (default: now)
  - Purpose: Timestamp of task creation
  - Constraints: Auto-generated on creation
- **updated_at**: DateTime (default: now)
  - Purpose: Timestamp of last update
  - Constraints: Auto-generated on update

### Validation Rules
1. **Title Required**: Task.title must not be empty or null
2. **Title Length**: Task.title must be between 1 and 200 characters
3. **Description Length**: Task.description, if provided, must be between 1 and 1000 characters
4. **User Ownership**: Each Task.user_id must reference a valid User.id
5. **ID Uniqueness**: Each Task.id must be unique within the system

### State Transitions
- **New Task**: When created, Task.completed = False by default
- **Mark Complete**: Task.completed transitions from False to True
- **Mark Incomplete**: Task.completed transitions from True to False

## Conversation Entity

### Attributes
- **id**: UUID (primary key)
  - Purpose: Unique identifier for each conversation
  - Constraints: Auto-generated UUID, not null, unique
- **user_id**: UUID (foreign key to User.id, required)
  - Purpose: Links conversation to the owning user
  - Constraints: References User.id, cascading delete
- **messages**: JSON (required)
  - Purpose: Stores the conversation history
  - Constraints: Array of message objects with role and content
- **created_at**: DateTime (default: now)
  - Purpose: Timestamp of conversation creation
  - Constraints: Auto-generated on creation
- **updated_at**: DateTime (default: now)
  - Purpose: Timestamp of last update
  - Constraints: Auto-generated on update

### Validation Rules
1. **User Ownership**: Each Conversation.user_id must reference a valid User.id
2. **Messages Format**: Conversation.messages must be a valid JSON array
3. **ID Uniqueness**: Each Conversation.id must be unique within the system

## Database Relationships

### User ↔ Task
- **Relationship**: One-to-Many (One user can have many tasks)
- **Constraint**: Foreign key from Task.user_id to User.id with cascade delete
- **Access Pattern**: Users can only access their own tasks

### User ↔ Conversation
- **Relationship**: One-to-Many (One user can have many conversations)
- **Constraint**: Foreign key from Conversation.user_id to User.id with cascade delete
- **Access Pattern**: Users can only access their own conversations

## Storage Operations

### User Operations
- **Create**: Insert new user record with hashed password
- **Read**: Retrieve user by email or ID (password hash not exposed in API responses)
- **Update**: Modify user properties (except password, which requires special handling)
- **Delete**: Remove user and all related tasks and conversations (due to cascade)

### Task Operations
- **Create**: Insert new task with current user's ID
- **Read**: Retrieve tasks filtered by user ID
- **Update**: Modify task properties for tasks owned by authenticated user
- **Delete**: Remove task owned by authenticated user

### Conversation Operations
- **Create**: Insert new conversation with current user's ID
- **Read**: Retrieve conversations filtered by user ID
- **Update**: Append new messages to conversation history
- **Delete**: Remove conversation owned by authenticated user