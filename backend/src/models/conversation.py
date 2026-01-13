# # backend/src/models/conversation.py
# from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
# from sqlalchemy import text
# from typing import Optional, List
# import uuid
# import json


# class Message(SQLModel):
#     role: str  # "user" or "assistant"
#     content: str
#     timestamp: str


# class ConversationBase(SQLModel):
#     messages: str = Field(default='[]')  # JSON string storing the message history


# class Conversation(ConversationBase, table=True):
#     id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
#     user_id: uuid.UUID = Field(foreign_key="user.id", ondelete="CASCADE")
#     created_at: str = Field(
#         sa_column=Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
#     )
#     updated_at: str = Field(
#         sa_column=Column(
#             DateTime,
#             nullable=False,
#             server_default=text("CURRENT_TIMESTAMP"),
#             onupdate=text("CURRENT_TIMESTAMP")
#         )
#     )

#     # Relationship
#     user: "User" = Relationship(back_populates="conversations")


# class ConversationCreate(ConversationBase):
#     pass


# class ConversationRead(ConversationBase):
#     id: uuid.UUID
#     user_id: uuid.UUID
#     created_at: str
#     updated_at: str

#     @property
#     def parsed_messages(self) -> List[Message]:
#         """Parse the JSON messages string into Message objects."""
#         try:
#             messages_data = json.loads(self.messages)
#             return [Message(**msg) for msg in messages_data]
#         except json.JSONDecodeError:
#             return []


# class ConversationUpdate(SQLModel):
#     messages: Optional[str] = None  # JSON string








# backend/src/models/conversation.py
from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from typing import Optional, List
from typing import TYPE_CHECKING
import uuid
import json

if TYPE_CHECKING:
    from .user import User


class Message(SQLModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: str


class ConversationBase(SQLModel):
    messages: str = Field(default='[]')  # JSON string storing the message history


class Conversation(ConversationBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # Fixed foreign key with cascade - changed to UUID type to match User.id
    user_id: uuid.UUID = Field(
        sa_column=Column(
            "user_id",
            PostgresUUID(as_uuid=True),
            ForeignKey("user.id", ondelete="CASCADE"),
            nullable=False
        )
    )

    created_at: str = Field(
        sa_column=Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    )
    updated_at: str = Field(
        sa_column=Column(
            DateTime,
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            onupdate=text("CURRENT_TIMESTAMP")
        )
    )

    # Relationship
    user: "User" = Relationship(back_populates="conversations")


class ConversationCreate(ConversationBase):
    pass


class ConversationRead(ConversationBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: str
    updated_at: str

    @property
    def parsed_messages(self) -> List[Message]:
        """Parse the JSON messages string into Message objects."""
        try:
            messages_data = json.loads(self.messages)
            return [Message(**msg) for msg in messages_data]
        except json.JSONDecodeError:
            return []


class ConversationUpdate(SQLModel):
    messages: Optional[str] = None  # JSON string
