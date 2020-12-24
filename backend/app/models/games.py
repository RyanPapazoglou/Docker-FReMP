from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from app.models.util.PyObjectId import PyObjectId


class Games(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    game: UUID = Field(...)
    favorite: str = Field(...)
    underdog: str = Field(...)
    date: datetime = Field(...)
    spread: int = Field()
    winner: str = Field()

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }