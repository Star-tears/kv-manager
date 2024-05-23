from fastapi import APIRouter

from app.api.routes import kv

api_router = APIRouter()
api_router.include_router(kv.router, prefix="/kv", tags=["kv"])
