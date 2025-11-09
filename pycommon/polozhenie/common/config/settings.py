from functools import lru_cache
from urllib.parse import quote

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = [
    "settings",
]


class S3Settings(BaseModel):
    host: str
    port: int
    username: str
    password: str


class KafkaSettings(BaseModel):
    host: str
    port: int


class DatabaseSettings(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database_name: str

    @property
    def uri(self) -> str:
        return f"mongodb://{quote(self.username)}:{quote(self.password)}@{self.host}:{self.port}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")
    s3: S3Settings
    kafka: KafkaSettings
    database: DatabaseSettings = Field(alias="DB")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
