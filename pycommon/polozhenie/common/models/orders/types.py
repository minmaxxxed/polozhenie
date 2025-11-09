from polozhenie.common.models.orders.blur import BlurOperation
from polozhenie.common.models.orders.text import TextOperation

__all__ = [
    "Operation",
]

type Operation = TextOperation | BlurOperation
