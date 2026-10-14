from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.configs.database import config

engine = create_async_engine(
    config.connection_string,
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with new_session() as session:
        yield session
