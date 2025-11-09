from typing import Literal

from pydantic import Field

from polozhenie.common.models.orders.base import BaseOperation
from polozhenie.common.models.orders.enums import OperationType

__all__ = [
    "BlurOperation",
]


class BlurOperation(BaseOperation):
    operation: Literal[OperationType.BLUR]
    radius: int = Field(gt=0, lt=100, default=1)
