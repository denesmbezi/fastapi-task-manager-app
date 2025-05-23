from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId
from enum import Enum



class TeamRole(str, Enum):
    ADMIN = "admin"
    TEAM_MEMBER = "team_member"


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    DELETED = "deleted"




class User(BaseModel):
    full_name: str = Field(..., title="Full Name", max_length=50)
    email: str = Field(..., title="Email", max_length=30)
    password: str = Field(..., title="Password", max_length=12)
    phone_number: str = Field(..., title="Phone Number", max_length=15)

class Task(BaseModel):
    title: str = Field(..., title="Title", max_length=50)
    description: str = Field(..., title="Description of the task", max_length=200)
    status: str = Field(..., title="Status of the task", max_length=20)

class Team(BaseModel):
    name: str = Field(..., title="Team Name", max_length=50)
    description: str = Field(..., title="Description of the team", max_length=200)
    members: List[User] = Field(..., title="Members of the team")
    tasks: List[Task] = Field(..., title="Tasks assigned to the team")
    role: TeamRole = Field(..., title="Role of the user in the team")
    created_at: Optional[str] = Field(None, title="Creation date of the team")
    updated_at: Optional[str] = Field(None, title="Last update date of the team")


class TeamInDB(Team):
    id: ObjectId = Field(default_factory=ObjectId, title="ID of the team")
    created_at: Optional[str] = Field(None, title="Creation date of the team")
    updated_at: Optional[str] = Field(None, title="Last update date of the team")



