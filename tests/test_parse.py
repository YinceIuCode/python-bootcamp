from datetime import date

import pytest

from shared.study_planner.parse import parse_csv


def test_parse_csv_valid_file(tmp_path):
    """Test parsing a valid CSV file."""
    # Create a temporary CSV file
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n"
                        "Math,5,2.0,2026-10-30\n"
                        "Physics,4,1.5,2026-10-28", encoding="utf-8")
    
    tasks = parse_csv(str(csv_file))
    
    assert len(tasks) == 2
    assert tasks[0].title == "Math"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 2.0
    assert tasks[0].deadline == date(2026, 10, 30)

def test_parse_csv_invalid_data_edge_case(tmp_path):
    """Edge case: CSV with invalid data format (e.g., string instead of int)."""
    csv_file = tmp_path / "bad_tasks.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n"
                        "Math,HIGH,2.0,2026-10-30\n", encoding="utf-8")
    
    with pytest.raises(ValueError) as excinfo:
        parse_csv(str(csv_file))
    
    assert "invalid row at line 2" in str(excinfo.value).lower()