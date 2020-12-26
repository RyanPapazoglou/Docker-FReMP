from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
from app.models.util.PyObjectId import PyObjectId
from bson.objectid import ObjectId


class UserBase(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    id: Optional[PyObjectId] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
