from typing import Optional

import pydantic
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

    @pydantic.root_validator(pre=True)
    def _set_id(cls, data):
        """Swap the field _id to id (this could be done with field alias, by setting the field as "_id"
        and the alias as "person_id", but can be quite confusing)"""
        document_id = data.get("_id")
        if document_id:
            data["id"] = document_id
        return data

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
