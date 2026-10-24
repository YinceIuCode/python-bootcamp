from datetime import date

from shared.contract import Task
from shared.study_planner.allocate import allocate


def test_allocate_normal_fit():
    """Test allocating tasks when available hours perfectly fit."""
    t1 = Task("Task 1", 5, 2.0, date(2026, 10, 30))
    t2 = Task("Task 2", 4, 3.0, date(2026, 10, 30))
    
    available_hours = 5.0 
    
    blocks = allocate([t1, t2], available_hours)
    
    assert len(blocks) == 2
    allocated_tasks = [b.task.title for b in blocks]
    assert "Task 1" in allocated_tasks
    assert "Task 2" in allocated_tasks


def test_allocate_not_enough_hours_edge_case():
    """Edge case: Not enough available hours to satisfy the task's effort."""
    t1 = Task("Huge Task", 5, 10.0, date(2026, 10, 30))
    
    available_hours = 3.0
    
    blocks = allocate([t1], available_hours)
    
    assert len(blocks) == 0


def test_allocate_partial_fit():
    """Test when only some tasks can be allocated due to time limits."""
    t1 = Task("Task 1", 5, 2.0, date(2026, 10, 30))
    t2 = Task("Task 2", 4, 3.0, date(2026, 10, 30))
    
    available_hours = 4.0
    
    blocks = allocate([t1, t2], available_hours)
    
    assert len(blocks) == 1
    assert blocks[0].task.title == "Task 1"