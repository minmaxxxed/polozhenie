from functools import lru_cache

from polozhenie.common.config import settings
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase


@lru_cache
def get_client() -> AsyncMongoClient:
    return AsyncMongoClient(settings.database.uri)


@lru_cache
def get_database() -> AsyncDatabase:
    return get_client().get_database(settings.database.database_name)
