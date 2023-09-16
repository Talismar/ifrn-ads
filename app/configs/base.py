from secrets import token_urlsafe
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl
from pydantic_core import Url


class AppBaseSettings(BaseSettings):
    SECRET_KEY: str = "asdasdasdasdasdacascasc"
    BASE_URL: AnyHttpUrl

    BACKEND_CORS_ORIGINS: list[Url] = [
        Url("http://localhost"),
        Url("http://localhost:8080"),
    ]

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
