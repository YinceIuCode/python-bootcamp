
from .models import Task


class InfeasiblePlan(Exception):
    def __init__ (self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self):      # ~~ Operator << overload in C++
        return f"Plan infeasible: need {self.needed_h}h, but you only have {self.available_h}h!"


def check_feasible(tasks:list[Task], available_h: float) -> None:
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
    # else:
    #     print ("OKE!!!")

# tasks = []
# tasks.append(Task("DSA exam", 3, 2.5, date(2026, 10, 17)))
# tasks.append(Task("Gym", 2, 1.5, date(2026, 10, 15)))
# tasks.append(Task("Sleep", 5, 8, date(2026, 10, 14)))

# check_feasible(tasks, 8)
