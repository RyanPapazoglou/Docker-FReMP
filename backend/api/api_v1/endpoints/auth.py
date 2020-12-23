from fastapi import APIRouter
from database import db
from models import Users

router = APIRouter()

# TODO Implement secure login/logout routes with current user capabilities