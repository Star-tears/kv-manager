from typing import Annotated, Generator

from app.core.db import Db
from fastapi import Depends
from sqlmodel import Session


def get_db() -> Generator[Session, None, None]:
    with Session(Db.engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
