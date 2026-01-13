# # backend/src/models/task.py
# from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
# from sqlalchemy import text, ForeignKey
# from typing import Optional
# import uuid


# class TaskBase(SQLModel):
#     title: str = Field(min_length=1, max_length=200)
#     description: Optional[str] = Field(default=None, max_length=1000)
#     completed: bool = Field(default=False)


# class Task(TaskBase, table=True):
#     id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
#     user_id: uuid.UUID = Field(
#         sa_column=Column(
#             uuid.UUID,
#             ForeignKey("user.id", ondelete="CASCADE"),
#             nullable=False
#         )
#     )
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
#     user: "User" = Relationship(back_populates="tasks")


# class TaskCreate(TaskBase):
#     pass


# class TaskRead(TaskBase):
#     id: uuid.UUID
#     user_id: uuid.UUID
#     created_at: str
#     updated_at: str


# class TaskUpdate(SQLModel):
#     title: Optional[str] = None
#     description: Optional[str] = None
#     completed: Optional[bool] = None






# backend/src/models/task.py
from sqlmodel import SQLModel, Field, Relationship, Column, DateTime
from sqlalchemy import text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PostgresUUID
from typing import Optional, Union
from typing import TYPE_CHECKING
from datetime import datetime
import uuid
from pydantic import field_validator

if TYPE_CHECKING:
    from .user import User


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)


class Task(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    user_id: uuid.UUID = Field(
        sa_column=Column(
            PostgresUUID(as_uuid=True),
            ForeignKey("user.id", ondelete="CASCADE"),
            nullable=False
        )
    )

    created_at: datetime = Field(
        sa_column=Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime,
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            onupdate=text("CURRENT_TIMESTAMP")
        )
    )

    # Relationship
    user: "User" = Relationship(back_populates="tasks")


class TaskCreate(TaskBase):
    pass


from pydantic import field_serializer

class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    @field_serializer('created_at')
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat()

    @field_serializer('updated_at')
    def serialize_updated_at(self, value: datetime) -> str:
        return value.isoformat()


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
