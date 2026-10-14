from typing import Any, TypeVar

from fastapi import Depends
from sqlalchemy import select, update, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseDAO:
    def __init__(self, model: type[T], session: AsyncSession = Depends(get_session)) -> int:
        self.session = session
        self.model = model

    async def create(self, obj: T) -> T:
        self.session.add(obj)
        await self.flush_and_refresh(obj)
        return obj

    async def get_by_id(self, obj_id: int) -> T | None:
        return await self.session.get(self.model, obj_id)

    async def get_all(self) -> list[T]:
        results = await self.session.execute(select(self.model))
        return list(results.scalars().all())

    async def update_by_id(self, obj_id: int, update_data: dict[str, Any]) -> None:
        query = update(self.model).where(self.model.id == obj_id).values(**update_data)
        await self.execute_query_and_flush(query)
        return await self.get_by_id(obj_id)

    async def delete_by_id(self, obj_id: int) -> T:
        obj = await self.get_by_id(obj_id)
        query = delete(self.model).where(self.model.id == obj_id)
        await self.execute_query_and_flush(query)
        return obj

    async def execute_query_and_flush(self, query) -> Result[Any]:
        result = await self.session.execute(query)
        await self.session.flush()
        return result

    async def flush_and_refresh(self, obj: T) -> T:
        await self.session.flush()
        await self.session.refresh(obj)
        return obj
