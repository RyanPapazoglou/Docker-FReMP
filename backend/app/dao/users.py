from typing import Any, Dict, Optional, Union

from app.database import db
from app.core.security import get_password_hash, verify_password
from app.models.users import Users
from app.models.util.PyObjectId import PyObjectId
from app.schemas.users import UserCreate, UserUpdate


class UsersDao():
    def authenticate(self, *, email: str, password: str) -> Optional[Users]:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_user_by_email(self, email: str) -> Optional[Users]:
        user = db.users.find_one({"email": email})
        if not user:
            return None
        return user

    def get_user_by_id(self, id: Optional[PyObjectId]) -> Optional[Users]:
        user = db.users.find_one({"_id": id})
        if not user:
            return None
        return user

    def add_user(self, user: Users):
        res = db.users.insert_one(user.dict(by_alias=True))
        return res

    def is_active(self, user: Users) -> bool:
        return user.is_active

    def is_superuser(self, user: Users) -> bool:
        return user.is_superuser


user = UsersDao()
