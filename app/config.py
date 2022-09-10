import os


class Config:
    API_TITLE = "MagNet API"
    API_VERSION = "v0.1"
    OPENAPI_VERSION = "3.0.2"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
