from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from app import dao
from app.database import db
from app.models import Users

router = APIRouter()

@router.get('/all')
async def get_users() -> Dict:
    users = []
    for user in db.users.find():
        users.append(Users(**user))
    return {'users': users}

# TODO add validators for unique usernames/emails
@router.post('/create')
async def create_user(user: Users) -> Dict:
    if hasattr(user, 'id'):
        delattr(user, 'id')
    exists = dao.users.get_user_by_email(user.email)
    if exists:
        raise HTTPException(status_code=400, detail="Email is taken, please use another.")
    ret = dao.users.add_user(user)
    user.id = ret.inserted_id
    return {'user': user}