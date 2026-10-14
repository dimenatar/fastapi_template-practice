from fastapi import HTTPException, status


class DatabaseConflictError(HTTPException):
    def __init__(self, message: str = "Database conflict error", status_code: int = status.HTTP_409_CONFLICT) -> None:
        super().__init__(status_code, message)


class EntityNotFoundError(HTTPException):
    def __init__(self, message: str = "Entity not found", status_code: int = status.HTTP_404_NOT_FOUND) -> None:
        super().__init__(status_code, message)
