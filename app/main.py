import logging

from app.api.v1 import router as api_v1_router
from app.core.app_factory import create_app
from app.core.configs.app_config import AppConfig

app_config = AppConfig()

logging.basicConfig(
    level=app_config.LOG_LEVEL,
    filename=app_config.LOG_FILE,
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)

app = create_app(
    routes=[api_v1_router],
    title="title",
    version="1",
)
