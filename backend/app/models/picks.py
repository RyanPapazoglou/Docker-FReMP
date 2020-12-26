from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from bson import ObjectId


class Picks(BaseModel):
    game: UUID = Field(...)
    team: str = Field(...)
    date: datetime = Field(...)
    username: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
