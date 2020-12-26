from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bson import ObjectId


class Games(BaseModel):
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