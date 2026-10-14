import asyncio
import os
import sys
from logging.config import fileConfig

from alembic import context
from alembic.script import ScriptDirectory
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from app.core.configs.database import DatabaseConfig
from app.models.base_model import BaseModel

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BaseModel.metadata

config.set_main_option("sqlalchemy.url", DatabaseConfig().connection_string + "?async_fallback=True")


def process_revision_directives(context, revision, directives):
    migration_script = directives[0]
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()

    if head_revision is None:
        new_rev_id = 1
    else:
        last_rev_id = int(head_revision.lstrip("0"))
        new_rev_id = last_rev_id + 1
    migration_script.rev_id = "{0:04}".format(new_rev_id)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        process_revision_directives=process_revision_directives,
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        connectable = create_async_engine(
            config.get_main_option("sqlalchemy.url"),
            poolclass=pool.NullPool,
        )

        loop.run_until_complete(run_async_migrations(connectable))
    finally:
        loop.close()
        asyncio.set_event_loop(None)


async def run_async_migrations(connectable: AsyncEngine) -> None:
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    context.configure(
        process_revision_directives=process_revision_directives,
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
