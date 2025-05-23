from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId
from enum import Enum



class UserRole(str, Enum):
    ADMIN = "admin"
    TEAM_MEMBER = "team_member"




class User(BaseModel):
    full_name: str = Field(..., title="Full Name", max_length=50)
    email: str = Field(..., title="Email", max_length=30)
    password: str = Field(..., title="Password", max_length=12)
    phone_number: str = Field(..., title="Phone Number", max_length=15)

class Task(BaseModel):
    title: str = Field(..., title="Title", max_length=50)
    description: str = Field(..., title="Description of the task", max_length=200)
    status: str = Field(..., title="Status of the task", max_length=20)

