from pydantic import PostgresDsn
from pydantic_settings import SettingsConfigDict

from app.core.configs.base import BaseConfig


class DatabaseConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="DB_")

    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    NAME: str

    @property
    def connection_string(self) -> str:
        return PostgresDsn(
            f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"
        ).unicode_string()


config = DatabaseConfig()
