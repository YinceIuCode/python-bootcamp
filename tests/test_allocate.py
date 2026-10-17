from datetime import date
from shared.contract import Task, Block
from shared.study_planner.allocate import allocate

def test_allocate_normal_fit():
    """Test allocating tasks when available hours perfectly fit."""
    t1 = Task("Task 1", 5, 2.0, date(2026, 10, 30))
    t2 = Task("Task 2", 4, 3.0, date(2026, 10, 30))
    
    available_hours = [3.0, 2.0]
    
    blocks = allocate([t1, t2], available_hours)
    
    assert len(blocks) == 2
    # Task 1 (importance 5) gets the 2.0 block
    # Task 2 (importance 4) gets the 3.0 block
    allocated_tasks = [b.task.title for b in blocks]
    assert "Task 1" in allocated_tasks
    assert "Task 2" in allocated_tasks

def test_allocate_not_enough_hours_edge_case():
    """Edge case: No available hours can satisfy the task's effort."""
    t1 = Task("Huge Task", 5, 10.0, date(2026, 10, 30))
    available_hours = [1.0, 2.0]
    
    # The current bisect logic might fail or return nothing if it can't find a fit.
    # We ensure it either safely returns an empty list or handles the logic gracefully.
    try:
        blocks = allocate([t1], available_hours)
        assert len(blocks) == 0
    except Exception as e:
        # If the bisect throws an UnboundLocalError (which it currently does for large values),
        # this test will fail, indicating a bug in allocate.py that the team needs to fix!
        pytest.fail(f"Allocate algorithm crashed on edge case: {e}")