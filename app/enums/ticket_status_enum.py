from enum import Enum


class TicketStatusEnum(Enum):
    """
    Enum représentant les différents statuts d'un ticket.
    Les statuts possibles incluent : ouvert, en cours, résolu, fermé, rouvert, en attente et annulé.
    """

    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REOPENED = "reopened"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"
