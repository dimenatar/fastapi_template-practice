from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import APIRouter, FastAPI, HTTPException

from app.errors.exception_handlers import custom_exception_handler


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield


handlers_to_exceptions: dict[Any, list[type[Exception]]] = {
    custom_exception_handler: [HTTPException],
}


def create_app(routes: list[APIRouter], **kwargs: Any) -> FastAPI:
    app = FastAPI(lifespan=lifespan, **kwargs)
    for handler, exceptions in handlers_to_exceptions.items():
        for exception in exceptions:
            app.exception_handler(exception)(handler)

    for route in routes:
        app.include_router(route)

    return app
