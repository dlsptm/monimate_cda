from enum import Enum


class TicketStatusEnum(Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REOPENED = "reopened"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"
