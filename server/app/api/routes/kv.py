import os
from app.api.deps import SessionDep
from app.common.config import Config
from app.models.kv_items import BucketItemBase, KvItemBase
from app.models.response import ResponseBase
from app.models.sql_models import KvData
from app.utils.resource import create_folder
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import JSONResponse

from app.utils import crud


router = APIRouter()


@router.get("/get_kv_data", response_model=ResponseBase)
def get_kv_data(data: BucketItemBase, session: SessionDep):
    kv_data = crud.get_kv(session, data.bucketName)
    return ResponseBase(code=0, data=kv_data)


@router.post("/update_kv", response_model=ResponseBase)
def update_kv(data: KvItemBase, session: SessionDep):
    kv_data = crud.upsert_kv(session, data.key, data.value, data.bucketName)
    return ResponseBase(code=0, data=kv_data)


@router.post("/create_bucket", response_model=ResponseBase)
def create_bucket(data: BucketItemBase):
    path = os.path.join(Config.WEBSERVER, "kv", "buckets", data.bucketName)
    result = create_folder(path)
    return ResponseBase(code=0, data={"result": result})
