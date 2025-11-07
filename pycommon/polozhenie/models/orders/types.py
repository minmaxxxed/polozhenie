from polozhenie.models.orders.blur import BlurOperation
from polozhenie.models.orders.text import TextOperation

__all__ = [
    "Operation",
]

type Operation = TextOperation | BlurOperation  # error: ignore[syntax]
