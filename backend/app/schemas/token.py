from typing import Optional

from pydantic import BaseModel

from app.models.util.PyObjectId import PyObjectId


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[PyObjectId] = None