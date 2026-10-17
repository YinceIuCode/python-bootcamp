from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a study task for Week 2."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Returns how many days are left until the deadline (never below 0)."""
        days = (self.deadline - today).days
        return max(days, 0)
