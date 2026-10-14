import uuid
from datetime import datetime

from sqlalchemy import DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr
from sqlalchemy.testing.schema import mapped_column

from app.utils import camel_to_snake


# pylint: disable=not-callable
class BaseModel(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # pylint: disable=no-self-argument
    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)
