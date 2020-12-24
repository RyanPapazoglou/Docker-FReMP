from fastapi import APIRouter
from app.database import db
from app.models import Picks

router = APIRouter()

@router.get('/all')
async def get_picks():
    picks = []
    for pick in db.picks.find():
        pick.append(Picks(**pick))
    return {'picks': picks}

@router.post('/create')
async def create_user(pick: Picks):
    if hasattr(pick, 'id'):
        delattr(pick, 'id')
    ret = db.picks.insert_one(pick.dict(by_alias=True))
    pick.id = ret.inserted_id
    return {'pick': pick}