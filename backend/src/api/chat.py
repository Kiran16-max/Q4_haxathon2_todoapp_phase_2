# backend/src/api/chat.py
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from typing import Dict, Any
from uuid import UUID
import json
from src.database import engine
from src.models.conversation import Conversation, ConversationCreate, ConversationRead, Message
from src.models.user import User
from src.utils.jwt_handler import get_current_user
from src.ai.chat_processor import process_chat_message

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.post("/chat")
def chat(
    message: str,
    conversation_id: UUID = None,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Process the chat message using AI
    response, tool_used = process_chat_message(
        user_id=current_user.id,
        message=message,
        conversation_id=conversation_id,
        session=session
    )
    
    return {
        "response": response,
        "conversation_id": conversation_id,
        "tool_used": tool_used
    }