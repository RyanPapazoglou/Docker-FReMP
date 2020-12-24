from fastapi import APIRouter
from app.database import db
from app.models import Games

router = APIRouter()

@router.get('/all')
async def get_users():
    games = []
    for game in db.game.find():
        games.append(Games(**game))
    return {'games': games}