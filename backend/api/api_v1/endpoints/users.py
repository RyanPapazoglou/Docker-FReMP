from fastapi import APIRouter
from database import db
from models import Users

router = APIRouter()

@router.get('/all')
async def get_users():
    users = []
    for user in db.users.find():
        users.append(Users(**user))
    return {'users': users}

# TODO add validators for unique usernames/emails
@router.post('/create')
async def create_user(user: Users):
    if hasattr(user, 'id'):
        delattr(user, 'id')
    ret = db.users.insert_one(user.dict(by_alias=True))
    user.id = ret.inserted_id
    return {'user': user}