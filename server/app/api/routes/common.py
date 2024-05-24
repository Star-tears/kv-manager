from app.models.response import ResponseBase
from fastapi import APIRouter


router = APIRouter()


@router.get("/get_version", response_model=ResponseBase)
def get_kv_data():
    return ResponseBase(code=0, data={"version": "0.1.0"})
