import subprocess
import sys
from pathlib import Path


def test_study_planner_e2e_with_sample_file() -> None:
    """End-to-end test verifying the CLI execution with an existing sample CSV file."""
    sample_csv = Path("samples/tasks.csv")

    cmd = [
        sys.executable,
        "-m",
        "shared.study_planner.parse",
        str(sample_csv),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    assert result.returncode == 0, f"CLI process failed: {result.stderr}"


def test_study_planner_e2e_integration(tmp_path: Path) -> None:
    """End-to-end test simulating CLI commands with dynamic task input."""
    test_csv = tmp_path / "test_tasks.csv"
    test_csv.write_text(
        "name,hours,due\n"
        "Math Assignment,2.0,tomorrow\n"
        "Physics Lab,1.0,in 3 days\n",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        "-m",
        "shared.study_planner.parse",
        str(test_csv),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    assert result.returncode == 0, f"CLI exited with code {result.returncode}"
    assert result.stderr == ""