"""Module for validating task plan feasibility based on available hours."""

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when the total task effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize the InfeasiblePlan exception.

        Args:
            needed_h: The total effort hours required.
            available_h: The total available hours.
        """
        self.needed_h = needed_h
        self.available_h = available_h

        super().__init__(self.__str__())

    def __str__(self) -> str:
        """Return a formatted error message."""
        return f"infeasible plan: needed {self.needed_h}h, but only {self.available_h}h available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Check whether the given tasks can be completed within the available hours.

    Args:
        tasks: A list of Task objects.
        available_h: The total available hours.

    Raises:
        InfeasiblePlan: If the total task effort exceeds available hours.
    """
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
