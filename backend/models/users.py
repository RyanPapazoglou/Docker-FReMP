from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional
from models.util.PyObjectId import PyObjectId

# TODO Add password field
class Users(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str = Field(...)
    username: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }