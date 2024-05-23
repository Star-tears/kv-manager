import os
from sqlmodel import SQLModel, create_engine

from app.common.config import Config
from app.models.sql_models import KvData, KvRecord


class Db:
    engine = None


def get_db_url():
    filePath = os.path.join(Config.WEBSERVER, "kv", "database", "data.db")
    return "sqlite:///" + str(filePath)


def update_engine():
    Db.engine = create_engine(get_db_url())
    SQLModel.metadata.create_all(Db.engine)
