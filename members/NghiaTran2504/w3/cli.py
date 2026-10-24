import argparse
import csv
import sys
from datetime import date
from pathlib import Path


def load_tasks(filepath: Path) -> list[dict]:
    """Load task records from a CSV file.

    Args:
        filepath: Path object pointing to the tasks CSV file.

    Returns:
        A list of Task dictionaries containing title, hours, and due date.
    """
    tasks = []
    with filepath.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append({
                "title": row["title"],
                "hours": float(row["effort_h"]),
                "due": date.fromisoformat(row["deadline"]),
            })
    return tasks


def schedule_tasks(tasks: list[dict], available_hours: float, today_date: date) -> list[dict]:
    """Schedule tasks due on or after today_date up to available_hours limit.

    Args:
        tasks: Candidate tasks list.
        available_hours: Maximum available hours for scheduling.
        today_date: Current anchor date.

    Returns:
        A list of scheduled tasks with assigned hours.
    """

    valid_tasks = [t for t in tasks if t["due"] >= today_date]
    valid_tasks.sort(key=lambda x: x["due"])

    scheduled = []
    remaining = available_hours

    for task in valid_tasks:
        if remaining <= 0:
            break
        allocated = min(task["hours"], remaining)
        scheduled.append({"title": task["title"], "hours": allocated})
        remaining -= allocated

    return scheduled


def main():
    """Run the study task scheduler CLI."""
    parser = argparse.ArgumentParser(description="Schedule study tasks for tonight.")
    parser.add_argument("filename", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available hours tonight")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Anchor date in YYYY-MM-DD format (default: today)",
    )

    parsed_args = parser.parse_args()

    if not parsed_args.filename.is_file():
        print(f"Error: File '{parsed_args.filename}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        tasks = load_tasks(parsed_args.filename)
    except (OSError, ValueError, KeyError, csv.Error) as e:
        print(f"Error reading file '{parsed_args.filename}': {e}", file=sys.stderr)
        sys.exit(1)

    scheduled = schedule_tasks(tasks, parsed_args.hours, parsed_args.today)

    print(f"Tonight ({parsed_args.hours:.1f} h):")
    for i, task in enumerate(scheduled, 1):
        dots = "." * max(1, 20 - len(task["title"]))
        print(f"{i}. {task['title']} {dots} {task['hours']:.1f} h")


if __name__ == "__main__":
    main()
