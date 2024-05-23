import os
from app.api.deps import SessionDep
from app.common.config import Config
from app.models.kv_items import BucketFile, BucketItemBase, KvItemBase
from app.models.response import ResponseBase
from app.models.sql_models import KvData
from app.utils.resource import create_folder, delete_folder
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse

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
    return ResponseBase(code=0, data={"message": f"Bucket create result: {result}"})


@router.post("/delete_bucket", response_model=ResponseBase)
def delete_bucket(data: BucketItemBase, session: SessionDep):
    path = os.path.join(Config.WEBSERVER, "kv", "buckets", data.bucketName)
    crud.delete_bucket(session, data.bucketName)
    result = delete_folder(path)
    return ResponseBase(code=0, data={"message": f"Bucket delete result: {result}"})


@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    try:
        # 需要使用filename替换file.filename，否则会500错误
        filename = file.filename
        # 指定保存文件的本地目录
        folder_path = os.path.join(Config.WEBSERVER, "uploads")
        file_path = os.path.join(Config.WEBSERVER, "uploads", filename)

        # 检查文件夹是否存在
        if not os.path.exists(folder_path):
            # 如果文件夹不存在，创建文件夹
            os.makedirs(folder_path)

        # 保存文件到本地
        with open(file_path, "wb") as buffer:
            contents = await file.read()
            buffer.write(contents)

        return JSONResponse(
            content={"message": "File uploaded successfully.", "file_path": file_path}
        )

    except Exception as e:
        # 处理可能出现的异常，比如文件写入失败
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        # 关闭文件，防止资源泄露
        await file.close()


@router.get("/download-file")
async def download_file(data: BucketFile):
    # 假设文件存储在"uploaded_files/"目录下
    file_path = os.path.join(
        Config.WEBSERVER, "kv", "buckets", data.bucketName, data.relativePath
    )
    # 检查文件是否存在
    if not os.path.exists(file_path):
        return {"error": "File not found."}
    # 返回文件，让客户端下载
    return FileResponse(
        file_path,
        media_type="application/octet-stream",
        filename=os.path.basename(file_path),
    )
