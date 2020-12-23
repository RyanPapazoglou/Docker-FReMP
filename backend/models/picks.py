from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from models.util.PyObjectId import PyObjectId


class Picks(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    game: UUID = Field(...)
    team: str = Field(...)
    date: datetime = Field(...)
    username: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }