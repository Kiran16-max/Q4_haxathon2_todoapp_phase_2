# backend/src/ai/chat_processor.py
from sqlmodel import Session
from uuid import UUID
import json
from src.mcp.server import MCPServer
from src.models.conversation import Conversation, Message

def process_chat_message(user_id: UUID, message: str, conversation_id: UUID, session: Session):
    """
    Process a chat message using AI and MCP tools.
    
    Args:
        user_id: The ID of the user sending the message
        message: The message content
        conversation_id: The ID of the conversation (optional, creates new if None)
        session: Database session
    
    Returns:
        tuple: (response_text, tool_used)
    """
    # Initialize MCP server with tools
    mcp_server = MCPServer(session, user_id)
    
    # Get or create conversation
    if conversation_id:
        conversation = session.get(Conversation, conversation_id)
        if not conversation or conversation.user_id != user_id:
            raise ValueError("Invalid conversation ID")
    else:
        # Create new conversation
        conversation = Conversation(user_id=user_id)
        session.add(conversation)
        session.commit()
        session.refresh(conversation)
    
    # Parse existing messages
    try:
        messages = json.loads(conversation.messages)
    except json.JSONDecodeError:
        messages = []
    
    # Add user message to conversation
    user_message = {
        "role": "user",
        "content": message,
        "timestamp": "2026-01-09T10:00:00Z"  # In real app, use current timestamp
    }
    messages.append(user_message)
    
    # Process message with AI (simulated)
    # In a real implementation, this would call the OpenAI API
    response_text, tool_used = simulate_ai_response(message, mcp_server)
    
    # Add assistant message to conversation
    assistant_message = {
        "role": "assistant",
        "content": response_text,
        "timestamp": "2026-01-09T10:00:01Z"  # In real app, use current timestamp
    }
    messages.append(assistant_message)
    
    # Update conversation with new messages
    conversation.messages = json.dumps(messages)
    session.add(conversation)
    session.commit()
    
    return response_text, tool_used

def simulate_ai_response(message: str, mcp_server: MCPServer):
    """
    Simulate AI response based on message content.
    In a real implementation, this would call the OpenAI API.
    """
    message_lower = message.lower()
    
    # Determine intent and call appropriate MCP tool
    if any(word in message_lower for word in ["add", "create", "new", "task"]):
        # Extract task details from message (simplified)
        # In a real implementation, this would use NLP to extract details
        task_title = "Sample task from AI"  # Extract from message
        response = mcp_server.call_tool("add_task", {"title": task_title})
        return f"I've added the task: {task_title}", "add_task"
    
    elif any(word in message_lower for word in ["list", "show", "view", "my tasks"]):
        response = mcp_server.call_tool("list_tasks", {})
        return f"Here are your tasks: {response}", "list_tasks"
    
    elif any(word in message_lower for word in ["complete", "done", "finish"]):
        # In a real implementation, we'd extract the task ID from the message
        task_id = "some-task-id"  # Extract from message
        response = mcp_server.call_tool("complete_task", {"task_id": task_id})
        return f"I've marked the task as complete: {response}", "complete_task"
    
    elif any(word in message_lower for word in ["delete", "remove"]):
        # In a real implementation, we'd extract the task ID from the message
        task_id = "some-task-id"  # Extract from message
        response = mcp_server.call_tool("delete_task", {"task_id": task_id})
        return f"I've deleted the task: {response}", "delete_task"
    
    elif any(word in message_lower for word in ["update", "change", "modify"]):
        # In a real implementation, we'd extract the task ID and new details from the message
        task_id = "some-task-id"  # Extract from message
        new_details = {"title": "Updated task"}  # Extract from message
        response = mcp_server.call_tool("update_task", {"task_id": task_id, "details": new_details})
        return f"I've updated the task: {response}", "update_task"
    
    else:
        # Default response for unrecognized intents
        return "I understand you're looking for help with your tasks. You can ask me to add, list, update, or complete tasks.", None