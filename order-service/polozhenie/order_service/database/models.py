from datetime import datetime
from typing import Annotated
from uuid import UUID

from beanie import Document, Indexed
from polozhenie.common.models.orders.types import Operation
from pydantic import Field

from polozhenie.order_service.database.enums import OrderStatus


class Order(Document):
    image_id: Annotated[UUID, Indexed(unique=True)]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None
    status: OrderStatus = OrderStatus.CREATED
    pipeline: list[Operation]

    class Settings:
        name = "orders"


document_models = [
    Order,
]
