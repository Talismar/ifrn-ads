from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import AppBaseSettings
from functools import lru_cache


class LocalSettings(AppBaseSettings):
    AUTHJWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    AUTHJWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 2
    AUTHJWT_ALGORITHM: str = "HS256"

    DATABASE_URL: str


@lru_cache()
def get_settings():
    print("Setting local")
    return LocalSettings(_env_file=(".env.local"))


settings = get_settings()

# ORM settings
engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
