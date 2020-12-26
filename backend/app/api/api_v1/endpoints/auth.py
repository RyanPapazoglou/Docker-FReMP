from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app import schemas, dao, models
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = dao.user.authenticate(
        email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not dao.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    print('token user', user)
    return {
        "access_token": security.create_access_token(
            user['_id'], expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }


@router.post("/test-token", response_model=schemas.User)
def test_token(current_user: models.Users = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
