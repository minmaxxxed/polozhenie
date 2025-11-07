from enum import StrEnum, auto

__all__ = [
    "OperationType",
]


class OperationType(StrEnum):
    TEXT = auto()
    BLUR = auto()
    UNKNOWN = auto()
