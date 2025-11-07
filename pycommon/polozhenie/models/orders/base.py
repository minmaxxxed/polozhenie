from pydantic import BaseModel

from polozhenie.models.orders.enums import OperationType

__all__ = [
    "BaseOperation",
]


class BaseOperation(BaseModel):
    operation: OperationType
