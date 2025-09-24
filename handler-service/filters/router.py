from fastapi import APIRouter

from filters.blur.router import router as blur_router

router = APIRouter(prefix="/filters")

router.include_router(blur_router)
