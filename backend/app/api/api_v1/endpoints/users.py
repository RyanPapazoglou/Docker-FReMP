from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Depends

from app import dao
from app.api import deps
from app.database import db
from app.models import Users
from app.schemas import UserCreate, User

router = APIRouter()

@router.get('/all')
async def get_users() -> Dict:
    users = []
    for user in db.users.find():
        users.append(Users(**user))
    return {'users': users}


@router.post('/create')
async def create_user(user: UserCreate) -> Dict:
    exists = dao.user.get_user_by_email(user.email)
    if exists:
        raise HTTPException(status_code=400, detail="Email is taken, please use another.")
    ret = dao.user.add_user(user)
    new_user = User(
        id=ret.inserted_id,
        name=user.name,
        username=user.username,
        email=user.email
    )
    return {'user': new_user}


@router.get("/me", response_model=User)
def read_user_me(
    current_user: Users = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user