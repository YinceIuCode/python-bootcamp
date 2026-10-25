"""Command-line interface tool for study planner task allocation."""

from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path

from .dates import parse_due


def main() -> None:
    """Execute the CLI application to parse arguments and display study schedule."""
    import argparse

    parser = argparse.ArgumentParser(description="Study planner CLI tool")
    parser.add_argument("tasks_file", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Allocated hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in YYYY-MM-DD format",
    )

    args = parser.parse_args()

    if args.today:
        try:
            today_date = date.fromisoformat(args.today)
        except ValueError:
            print(
                f"Error: Invalid date format '{args.today}'. Use YYYY-MM-DD.",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        today_date = date.today()

    file_path = Path(args.tasks_file)
    if not file_path.exists():
        print(f"Error: File '{args.tasks_file}' not found.", file=sys.stderr)
        sys.exit(1)

    tasks: list[tuple[str, date, float]] = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 3:
                continue
            title = row[0].strip()
            if title.lower() in ["title", "task", "name"]:
                continue
            due_str = row[1].strip()
            try:
                hours = float(row[2].strip())
            except ValueError:
                hours = 1.0

            try:
                due_date = parse_due(due_str, today_date)
            except Exception:
                try:
                    due_date = date.fromisoformat(due_str)
                except Exception:
                    due_date = date.max

            if not isinstance(due_date, date):
                due_date = date.max

            tasks.append((title, due_date, hours))

    # Sắp xếp ưu tiên: 1. Hạn chót gần nhất -> 2. Thời lượng ngắn hơn -> 3. Tên theo bảng chữ cái
    tasks.sort(key=lambda x: (x[1], x[2], x[0]))

    print(f"Planning for date: {today_date.isoformat()}")
    print(f"Tonight ({args.hours:.1f} h):")

    allocated_hours = 0.0
    for title, _, task_hours in tasks:
        if allocated_hours + task_hours <= args.hours:
            print(f"- {title}")
            allocated_hours += task_hours
        elif allocated_hours == 0:
            print(f"- {title}")
            allocated_hours += task_hours
            break


if __name__ == "__main__":
    main()