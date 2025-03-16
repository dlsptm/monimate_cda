import enum


class GoalStatusEnum(enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    completed = "completed"
    overdue = "overdue"
    failed = "failed"
