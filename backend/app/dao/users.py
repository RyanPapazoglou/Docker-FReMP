from typing import Any, Dict, Optional, Union

from app.database import db
from app.core.security import get_password_hash, verify_password
from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate


class UsersDao():
    def authenticate(self, *, email: str, password: str) -> Optional[Users]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user