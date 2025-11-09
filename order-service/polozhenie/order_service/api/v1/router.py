from fastapi import APIRouter

from polozhenie.order_service.api.v1.orders.router import router as orders_router

router = APIRouter(prefix="/v1")

router.include_router(orders_router)
