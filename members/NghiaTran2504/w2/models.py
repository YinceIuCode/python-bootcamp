'''
C++
struct Task {
    std::string title;
    int importance;
    double effort_h;
};
'''

# Python
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        days_remaining = (self.deadline - today).days
        return max(0, days_remaining)

# current_day = date(2026, 10,14)
# deadline = date(2026, 10, 17)
# t = Task("Learn python", 3, 2.0, deadline)
# print (t.days_left(current_day))
# print (t)