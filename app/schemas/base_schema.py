import uuid
from datetime import datetime
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class BaseResponse(BaseModel):
    message: str | None = None
    error: str | None = None
    payload: T | None = None


class ModelBaseResponse(BaseModel):
    id: uuid.UUID


class ModelBaseDetailedResponse(ModelBaseResponse):
    updated_at: datetime
    created_at: datetime
