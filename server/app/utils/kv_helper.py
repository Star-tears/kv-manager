import os
import zipfile
from sqlmodel import Session
import app.utils.crud as crud


def gen_ts(session: Session, lang: str, path: str):
    """
    生成ts文件
    """
    gen_kv = crud.get_gen_kv(session, lang)
    with open(path, "w", encoding="utf-8") as file:
        for kv in gen_kv:
            if kv["value"] is None:
                kv["value"] = ""
            print(
                kv["key"] + "~-~" + kv["value"], file=file
            )  # print函数的file参数指定输出到的文件


def zip_dir(dir_path, output_zip_path):
    """
    将指定目录下的所有文件和子目录打包到一个zip文件中。

    :param dir_path: 要打包的目录路径
    :param output_zip_path: 输出的zip文件路径
    """
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_path):
            # 遍历目录树，将每个文件添加到zip文件中
            for file in files:
                file_path = os.path.join(root, file)
                # 使用相对路径确保zip文件内的结构正确
                relative_path = os.path.relpath(file_path, dir_path)
                zipf.write(file_path, relative_path)
