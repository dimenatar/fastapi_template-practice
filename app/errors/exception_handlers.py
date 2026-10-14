from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.schemas.base_schema import BaseResponse


async def custom_exception_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content=BaseResponse(error=str(exc.detail)))
