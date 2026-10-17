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
        return max(int((self.deadline - today).total_seconds() / 86400), 0)

# A = Task("bad", 9, 1.0, date(2026, 10, 30))
# print(A.days_left(date(2026, 10, 26)))