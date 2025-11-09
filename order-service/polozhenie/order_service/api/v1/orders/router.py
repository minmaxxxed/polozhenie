from uuid import UUID

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from polozhenie.order_service.api.v1.orders.schemas import CreateOrderRequest, CreateOrderResponse, OrderOut
from polozhenie.order_service.database.models import Order

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(image_id: UUID, request: CreateOrderRequest) -> CreateOrderResponse:
    if await Order.find_one(Order.image_id == image_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Order already exists",
        )

    order = Order(
        image_id=image_id,
        pipeline=request.pipeline,
    )

    await Order.insert(order)

    return CreateOrderResponse(order_id=order.id)


@router.get("/{order_id}", status_code=status.HTTP_200_OK)
async def get_order(order_id: PydanticObjectId) -> OrderOut:
    if not (order := await Order.find_one(Order.id == order_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    return OrderOut(
        order_id=order_id,
        image_id=order.image_id,
        status=order.status,
        pipeline=order.pipeline,
    )
