import logging

from api.v1 import router as api_v1_router
from core.app_factory import create_app
from core.configs.app_config import AppConfig

logging.basicConfig(
    level=AppConfig.LOG_LEVEL,
    filename=AppConfig.LOG_FILE,
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)

app = create_app(
    routes=[api_v1_router],
    title="title",
    version="1",
)
