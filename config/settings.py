from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from common.dot_env_loader import dot_env_loader

# Load the .env file before loading the settings
dot_env_loader()


class Settings(BaseSettings):
    """Settings for the application."""

    model_config = SettingsConfigDict(extra="ignore", env_ignore_empty=True)

    # Database settings
    db_connection: str = Field(default="postgresql")
    db_host: str = Field(default="localhost")
    db_port: int = Field(default=5432)
    db_user: str = Field(default="postgres")
    db_password: str = Field(default="")
    db_name: str = Field(default="postgres")
    db_sslmode: str = Field(default="prefer")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Get the settings.

    Cached to avoid re-reading the environment variables on each call.
    """
    return Settings()


settings = get_settings()