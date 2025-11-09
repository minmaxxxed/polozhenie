from contextlib import asynccontextmanager

from beanie import init_beanie
from fastapi import FastAPI

from polozhenie.order_service.api.v1.router import router as v1_router
from polozhenie.order_service.database.client import get_database
from polozhenie.order_service.database.models import document_models


@asynccontextmanager
async def lifespan(_: FastAPI):  # noqa: ANN201
    await init_beanie(database=get_database(), document_models=document_models)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(v1_router)
