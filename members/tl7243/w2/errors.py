from .models import Task


class InfeasiblePlan(Exception):
	def __init__(self, needed_h: float, available_h: float) -> None:
		self.needed_h = needed_h
		self.available_h = available_h
		super().__init__(
			f"Infeasible plan: needed {needed_h}h, but only {available_h}h available."
		)

def check_feasible(tasks: list[Task], available_h: float) -> None:
	needed = sum(task.effort_h for task in tasks)
	if needed > available_h:
		raise InfeasiblePlan(needed, available_h)
