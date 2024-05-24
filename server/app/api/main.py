from fastapi import APIRouter

from app.api.routes import common, kv

api_router = APIRouter()
api_router.include_router(kv.router, prefix="/kv", tags=["kv"])
api_router.include_router(common.router, prefix="/common", tags=["common"])
