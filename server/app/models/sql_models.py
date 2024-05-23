from datetime import datetime

from typing import Optional

from sqlmodel import Field, SQLModel


class KvData(SQLModel, table=True):
    key: str = Field(primary_key=True)
    value: str
    updated_at: Optional[datetime] = Field(
        default=datetime.now(),
        sa_column_kwargs={"onupdate": datetime.now()},
        nullable=False,
    )
    bucket: Optional[str] = Field(default=None, nullable=True)


class KvRecord(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": True}
    )
    key: str
    value: str
    updated_at: Optional[datetime] = Field(
        default=datetime.now(),
        nullable=False,
    )
    bucket: Optional[str] = Field(default=None, nullable=True)
