from uuid import UUID

from beanie import PydanticObjectId
from polozhenie.common.models.orders.types import Operation
from pydantic import BaseModel, Field

from polozhenie.order_service.database.enums import OrderStatus


class CreateOrderRequest(BaseModel):
    pipeline: list[Operation] = Field(min_length=1, max_length=10)


class CreateOrderResponse(BaseModel):
    order_id: PydanticObjectId


class OrderOut(BaseModel):
    order_id: PydanticObjectId
    image_id: UUID
    status: OrderStatus
    pipeline: list[Operation]
