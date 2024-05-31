from datetime import datetime

from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class KvId(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": True}
    )
    kv_items: list["KvData"] = Relationship(
        back_populates="item", sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    kv_records_items: list["KvRecord"] = Relationship(
        back_populates="item", sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )


class KvData(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": True}
    )
    value: str
    language: str
    kv_id: int = Field(foreign_key="kvid.id", nullable=False)
    item: "KvId" = Relationship(back_populates="kv_items")
    updated_at: datetime


class KvRecord(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": True}
    )
    value: str
    language: str
    kv_id: int = Field(foreign_key="kvid.id", nullable=False)
    item: "KvId" = Relationship(back_populates="kv_records_items")
    updated_at: datetime


class Language(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": True}
    )
    lang: str
    feishu_language: str
