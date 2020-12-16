from typing import Optional, Dict
from fastapi import FastAPI
from api.api_v1.api import api_router

app = FastAPI(
    title='TEST', openapi_url=f"/api/v1/openapi.json"
)

app.include_router(api_router, prefix="/api/v1")