from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional
from app.models.util.PyObjectId import PyObjectId


class Users(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
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
