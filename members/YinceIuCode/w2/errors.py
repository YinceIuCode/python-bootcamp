class InfeasiblePlan(Exception):
    """Custom exception raised when required hours exceed available hours."""

    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        message = (
            f"Infeasible plan: required {needed_h}h, but only {available_h}h available."
        )
        super().__init__(message)


def check_feasible(tasks: list, available_h: float):
    """Checks if the total effort of tasks is within the available hours."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
