import sys

print("\n", sys.path, "\n")


from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h : float, available_h : float):
        self.needed_h : float = needed_h
        self.available_h : float = available_h
        
    def __str__(self):
        return f"{self.needed_h} hour(s) is over {self.available_h} available hour(s)."

def check_feasible(tasks : list[Task], available_h : float) -> None:
    sorted_tasks = sorted(tasks, key = lambda task : task.deadline)
    total_required_day_h = 0
    
    for task_index in range(len(sorted_tasks) + 1):
        if task_index == 0:
            total_required_day_h += tasks[0].effort_h
            continue
        
        if task_index == len(tasks) or tasks[task_index].deadline != tasks[task_index - 1].deadline:
            if (total_required_day_h > available_h):
                raise InfeasiblePlan(total_required_day_h, available_h)

            total_required_day_h = 0 if task_index == len(tasks) else tasks[task_index].effort_h
            continue
            
        total_required_day_h += tasks[task_index].effort_h
    
