from typing import Any
from pydantic import BaseModel


class ResponseBase(BaseModel):
    type: str | None = "response"
    code: int = 0
    data: Any
