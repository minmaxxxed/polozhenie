from fastapi import FastAPI

from filters.router import router as filters_router

app = FastAPI()

app.include_router(filters_router)
