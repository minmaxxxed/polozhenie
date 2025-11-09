from enum import StrEnum, auto


class OrderStatus(StrEnum):
    CREATED = auto()
    ON_MODERATION = auto()
    MODERATION_FAILED = auto()
    MODERATION_PASSED = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    FAILED = auto()
