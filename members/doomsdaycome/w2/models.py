"""Module defining the Task data model and associated operations."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Represents a scheduled task with title, importance, effort, and deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate task attributes after initialization.

        Raises:
            ValueError: If importance is not between 1 and 5 inclusive.
        """
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate the number of days remaining until the deadline from a given date.

        Args:
            today: The current reference date.

        Returns:
            The number of days left (minimum 0).
        """
        return max((self.deadline - today).days, 0)
