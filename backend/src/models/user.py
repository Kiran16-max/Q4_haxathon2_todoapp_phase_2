# backend/src/models/user.py
from sqlmodel import SQLModel, Field, Column, DateTime, Relationship
from sqlalchemy import text
from typing import Optional, List
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from .task import Task
    from .conversation import Conversation


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)
    name: Optional[str] = Field(default=None, max_length=255)


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: str = Field(nullable=False)
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

    # Relationships
    tasks: List["Task"] = Relationship(back_populates="user")
    conversations: List["Conversation"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: uuid.UUID
    created_at: str
    updated_at: str


class UserUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None