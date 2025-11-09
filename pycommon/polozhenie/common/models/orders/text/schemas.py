from typing import Literal

from pydantic import BaseModel, Field

from polozhenie.common.models.orders.base import BaseOperation
from polozhenie.common.models.orders.enums import OperationType
from polozhenie.common.models.orders.text.enums import Font

__all__ = [
    "TextOperation",
    "TextPosition",
]


class TextPosition(BaseModel):
    x: int
    y: int


class TextOperation(BaseOperation):
    operation: Literal[OperationType.TEXT]
    font: Font = Field(default=Font.IMPACT)
    size: int = Field(gt=0, lt=100, default=20)
    text: str
    position: TextPosition
