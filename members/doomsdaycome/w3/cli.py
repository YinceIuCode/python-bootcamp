import argparse
import sys
from datetime import date

from ..w2.io_utils import load_tasks


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan tasks for tonight")
    parser.add_argument("path")
    parser.add_argument("--hours", type=float)
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())

    args = parser.parse_args()

    try:
        tasks = load_tasks(args.path)
    except FileNotFoundError:
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.hours < 0:
        print("error: hours must be non-negative")
        return 1

    tasks.sort(
        key=lambda task: (
            -(task.importance / task.effort_h) if task.effort_h > 0 else float("-inf"),
            task.deadline,
        )
    )

    selected = []
    remaining = args.hours

    for task in tasks:
        if task.effort_h <= remaining:
            selected.append(task)
            remaining -= task.effort_h

    print(f"Tonight ({args.hours:.1f} h):")

    if not selected:
        print("No tasks fit the available time.")
        return 0

    for i, task in enumerate(selected, start=1):
        print(f"{i}. {task.title:.<20} {task.effort_h:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())
