from fastapi import APIRouter

from api.api_v1.endpoints import users, picks, games

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(picks.router, prefix="/picks", tags=["picks"])
api_router.include_router(games.router, prefix="/games", tags=["games"])