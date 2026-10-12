from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    def __init__(self, title : str, importance : int, effort_h : float, deadline : date):
        self.title: str = title
        self.importance: int = importance
        self.effort_h: float = effort_h
        self.deadline: date = deadline
    
    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
        
    def days_left(self, today: date) -> int:
        return max(int((today - self.deadline).total_seconds() / 86400), 0)
