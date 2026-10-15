from .models import Task


class InfeasiblePlan(Exception):
    """Custom exception raised when task workload exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: needed {needed_h}h, but only {available_h}h available."
        )


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Check whether the total required hours exceed available hours."""
    total_needed = sum(task.effort_h for task in tasks)
    if total_needed > available_h:
        raise InfeasiblePlan(needed_h=total_needed, available_h=available_h)