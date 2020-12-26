from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

from app.models.util.PyObjectId import PyObjectId


class Users(BaseModel):
    name: str = Field(...)
    username: str = Field(...)
    email: EmailStr = Field(...)
    hashed_password: str = Field(...)
    is_active: bool = Field(True)
    is_superuser: bool = Field(False)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
