"""End-to-end tests for the shared study_planner CLI package."""

from pathlib import Path
import subprocess
import sys

BOOTCAMP = Path(__file__).resolve().parents[1]


def test_study_planner_e2e_with_sample_file() -> None:
    """End-to-end test verifying CLI execution with the sample CSV file."""
    sample_csv = BOOTCAMP / "samples" / "tasks.csv"

    cmd = [
        sys.executable,
        "-m",
        "shared.study_planner",
        str(sample_csv),
        "--hours",
        "2",
        "--today",
        "2026-10-26",
    ]

    result = subprocess.run(
        cmd, capture_output=True, text=True, check=False, cwd=BOOTCAMP
    )

    assert result.returncode == 0, f"CLI process failed: {result.stderr}"
    assert "Assignment" in result.stdout
    assert "Total Allocated Hours: 1.5h" in result.stdout


def test_study_planner_e2e_integration(tmp_path: Path) -> None:
    """End-to-end test simulating CLI execution with dynamic CSV task input."""
    test_csv = tmp_path / "test_tasks.csv"
    test_csv.write_text(
        "title,importance,effort_h,deadline\n"
        "Math Assignment,5,2.0,2026-10-27\n"
        "Physics Lab,3,1.0,2026-10-29\n",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        "-m",
        "shared.study_planner",
        str(test_csv),
        "--hours",
        "3",
        "--today",
        "2026-10-26",
    ]

    result = subprocess.run(
        cmd, capture_output=True, text=True, check=False, cwd=BOOTCAMP
    )

    assert result.returncode == 0, f"CLI exited with code {result.returncode}"
    assert "Math Assignment" in result.stdout
    assert "Physics Lab" in result.stdout
    assert "Total Allocated Hours: 3.0h" in result.stdout