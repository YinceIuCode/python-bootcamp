from datetime import date
from shared.contract import Task
from shared.study_planner.prioritize import prioritize

def test_prioritize_normal_tasks():
    """Test prioritizing tasks based on importance and days left."""
    today = date(2026, 10, 20)
    
    # days_left = 10, score = 3 / 10 = 0.3
    t1 = Task("Low Priority", 3, 2.0, date(2026, 10, 30))
    # days_left = 2, score = 5 / 2 = 2.5
    t2 = Task("High Priority", 5, 2.0, date(2026, 10, 22))
    
    result = prioritize([t1, t2], today)
    
    # t2 should be first because of a higher score
    assert result[0].title == "High Priority"
    assert result[1].title == "Low Priority"

def test_prioritize_past_deadline_edge_case():
    """Edge case: Task deadline is today or in the past (days_left <= 0)."""
    today = date(2026, 10, 20)
    
    # days_left = -5 -> bounded to 1 -> score = 4 / 1 = 4.0
    t_past = Task("Past Due", 4, 1.0, date(2026, 10, 15))
    # days_left = 1 -> score = 3 / 1 = 3.0
    t_future = Task("Tomorrow", 3, 1.0, date(2026, 10, 21))
    
    result = prioritize([t_past, t_future], today)
    
    assert result[0].title == "Past Due"