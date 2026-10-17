from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_render_normal_blocks():
    """Test rendering a valid list of study blocks."""
    t1 = Task("Math", 5, 2.0, date(2026, 10, 30))
    b1 = Block(task=t1, hours=2.0)
    
    output = render([b1])
    
    assert "=== Study Planner Blocks ===" in output
    assert "Task: Math" in output
    assert "Allocated: 2.0h" in output
    assert "Total Allocated Hours: 2.0h" in output

def test_render_empty_blocks_edge_case():
    """Edge case: Rendering an empty list of blocks."""
    output = render([])
    assert output == "No blocks to render."