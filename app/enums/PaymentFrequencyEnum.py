import enum

class PaymentFrequencyEnum(enum.Enum):
    once = "once"
    weekly = "weekly"
    biweekly = "biweekly"
    monthly = "monthly"
    bimonthly = "bimonthly"
    quarterly = "quarterly"
    semiannually = "semiannually"
    yearly = "yearly"