import sys
from datetime import date
from pathlib import Path

curr_dir = Path(__file__).resolve().parents[2]
if str(curr_dir) not in sys.path:
        sys.path.insert(0, str(curr_dir))

from shared.contract import Task


def prioritise_score(t: Task, today: date) -> float:
    days_left = max(1, (t.deadline - today).days)
    return t.importance/days_left

def prioritise(tasks:list[Task], today:date) -> list[Task]:

    def get_prioritise_score(task: Task) -> float:
        return prioritise_score(task, today)

    prioritise_list = sorted(tasks, key=get_prioritise_score, reverse=True)
    return prioritise_list


