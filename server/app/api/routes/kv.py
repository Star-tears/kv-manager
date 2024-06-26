import time
import os
from app.api.deps import SessionDep
from app.common.config import Config
from app.models.kv_items import (
    KvIdItem,
    KvItem,
    KvRecordItem,
    LangKv,
    LangWithPath,
    LanguageItemBase,
)
from app.models.response import ResponseBase
from app.utils.resource import (
    create_folder,
    delete_folder,
    get_folder_list,
    rename_file,
)
import app.utils.kv_helper as kv_helper
import app.utils.feishu_helper as feishu_helper
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse

from app.utils import crud


router = APIRouter()


@router.post("/delete_lang", response_model=ResponseBase)
def delete_lang(data: LanguageItemBase, session: SessionDep):
    crud.delete_language(session, data.lang)
    return ResponseBase(code=0, data={})


@router.get("/get_lang_list", response_model=ResponseBase)
def get_lang_list(session: SessionDep):
    result = crud.get_lang_list(session)
    return ResponseBase(code=0, data=result)


@router.post("/update_kv", response_model=ResponseBase)
def update_kv(data: KvItem, session: SessionDep):
    kv_data = crud.upsert_kv(
        session, data.key, data.value, data.langKey, data.langValue, data.kvId
    )
    return ResponseBase(code=0, data=kv_data)


@router.post("/get_kv_data", response_model=ResponseBase)
def get_kv_data(data: LangKv, session: SessionDep):
    kv_data = crud.get_kv(session, data.langKey, data.langValue)
    return ResponseBase(code=0, data=kv_data)


@router.post("/get_kv_record", response_model=ResponseBase)
def get_kv_record(data: KvRecordItem, session: SessionDep):
    kv_record = crud.get_kv_record(session, data.langValue, data.kvId)
    return ResponseBase(code=0, data=kv_record)


@router.post("/delete_kv", response_model=ResponseBase)
def delete_kv(data: KvIdItem, session: SessionDep):
    msg = crud.delete_kv(session, data.kvId)
    return ResponseBase(code=0, data={"msg": msg})


@router.post("/get_all_null_value_kv", response_model=ResponseBase)
def get_all_null_value_kv(data: LanguageItemBase, session: SessionDep):
    langList = crud.get_lang_list(session)
    null_kv_data = []
    for lang in langList:
        kv_data = crud.get_null_value_kv(session, data.lang, lang.lang)
        for kv in kv_data:
            kv["lang_value"] = lang.lang
        null_kv_data.extend(kv_data)
    return ResponseBase(code=0, data=null_kv_data)


@router.post("/upload_new_lang", response_model=ResponseBase)
def upload_new_lang(data: LangWithPath, session: SessionDep):
    crud.create_lang(session, "English", "en")
    file_path = os.path.join(Config.WEBSERVER, "uploads", data.path)
    try:
        kv_map = {}
        langValueIsCreated = False
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                kv_list = [s.strip() for s in line.split("~-~")]
                if len(kv_list) == 2:
                    kv_map[kv_list[0]] = kv_list[1]
                    if not langValueIsCreated and len(kv_list[1]) > 0:
                        langValue = feishu_helper.text_detect(kv_list[1])
                        crud.create_lang(session, data.lang, langValue)
                        langValueIsCreated = True
        for k, v in kv_map.items():
            crud.upsert_kv_with_no_commit(session, k, v, "English", data.lang)
        session.commit()
        msg = "Upload successfully"
    except Exception as e:
        msg = e
    return ResponseBase(code=0, data={"msg": msg})


@router.post("/gen_ts", response_model=ResponseBase)
def gen_ts(data: LanguageItemBase, session: SessionDep):
    file_path = os.path.join("ts", f"{data.lang}.ts")
    path = os.path.join(Config.WEBSERVER, "kv", "downloads", file_path)
    kv_helper.gen_ts(session, data.lang, path)
    return ResponseBase(code=0, data={"file_path": f"{file_path}"})


@router.post("/merge_check", response_model=ResponseBase)
def merge_check(data: LangWithPath, session: SessionDep):
    file_path = os.path.join(Config.WEBSERVER, "uploads", data.path)
    kv_map = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            kv_list = [s.strip() for s in line.split("~-~")]
            if len(kv_list) == 2:
                kv_map[kv_list[0]] = kv_list[1]
    merge_check_list = []
    id = 0
    for k, v in kv_map.items():
        curr_v = crud.get_v_by_k(session, k, data.lang)
        if curr_v != v:
            id += 1
            merge_check_list.append(
                {
                    "id": id,
                    "key": k,
                    "curr_value": curr_v,
                    "new_value": v,
                    "lang_key": "English",
                    "lang_value": data.lang,
                }
            )
    return ResponseBase(code=0, data=merge_check_list)


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


@router.get("/download-file/{filePath:path}")
async def download_file(filePath: str):
    # todo
    file_path = os.path.join(Config.WEBSERVER, "kv", "downloads", filePath)
    # 检查文件是否存在
    if not os.path.exists(file_path):
        return {"error": "File not found."}
    # 返回文件，让客户端下载
    return FileResponse(
        file_path,
        media_type="application/octet-stream",
        filename=os.path.basename(file_path),
    )


@router.get("/download-all-with-zip/{filename}")
async def download_all_with_zip(filename: str, session: SessionDep):
    folder_path = os.path.join(Config.WEBSERVER, "kv", "downloads", "ts")
    delete_folder(folder_path)
    create_folder(folder_path)
    langList = crud.get_lang_list(session)
    for el in langList:
        lang = el.lang
        if lang == "English":
            continue
        file_path = os.path.join("ts", f"{lang}.ts")
        path = os.path.join(Config.WEBSERVER, "kv", "downloads", file_path)
        kv_helper.gen_ts(session, lang, path)
    zip_path = os.path.join(Config.WEBSERVER, "kv", "downloads", "package", filename)
    kv_helper.zip_dir(os.path.join(Config.WEBSERVER, "kv", "downloads", "ts"), zip_path)
    # 检查文件是否存在
    if not os.path.exists(zip_path):
        return {"error": "File not found."}
    # 返回文件，让客户端下载
    return FileResponse(
        zip_path,
        media_type="application/octet-stream",
        filename=os.path.basename(zip_path),
    )
