from fastapi import APIRouter

from app.api.api_v1.endpoints import users, games, picks, auth

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(picks.router, prefix="/picks", tags=["picks"])
api_router.include_router(games.router, prefix="/games", tags=["games"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
