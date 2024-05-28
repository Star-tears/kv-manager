from sqlmodel import Session
import app.utils.crud as crud


def gen_ts(session: Session, lang: str, path: str):
    """
    生成ts文件
    """
    gen_kv = crud.get_gen_kv(session, lang)
    with open(path, "w", encoding="utf-8") as file:
        for kv in gen_kv:
            print(
                kv["key"] + "~-~" + kv["value"], file=file
            )  # print函数的file参数指定输出到的文件
