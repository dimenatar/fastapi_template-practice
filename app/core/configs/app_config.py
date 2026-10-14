import logging

from pydantic_settings import SettingsConfigDict

from app.core.configs.base import BaseConfig


class AppConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="APP_")

    LOG_LEVEL: int = logging.INFO
    LOG_FILE: str
