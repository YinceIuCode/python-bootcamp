import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class StudyTask:
    """Represent a study task loaded from CSV."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def days_left(self, today: date) -> int:
        """Return remaining days until deadline (minimum 1)."""
        return max(1, (self.deadline - today).days)


def load_tasks(path: Path) -> list[StudyTask]:
    """Load study tasks from a CSV file."""
    tasks: list[StudyTask] = []
    with path.open(mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)
        for line_num, row in enumerate(reader, start=2):
            if not row or all(not cell.strip() for cell in row):
                continue
            try:
                tasks.append(
                    StudyTask(
                        title=row[0].strip(),
                        importance=int(row[1].strip()),
                        effort_h=float(row[2].strip()),
                        deadline=date.fromisoformat(row[3].strip()),
                    )
                )
            except (ValueError, IndexError) as err:
                raise ValueError(f"Invalid row at line {line_num}: {err}") from err
    return tasks


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI tool."""
    parser = argparse.ArgumentParser(description="Personal Study Planner CLI")
    parser.add_argument("path", type=Path, help="Path to the tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available hours")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the study planner CLI tool and return the exit status code."""
    args = build_parser().parse_args(argv)

    if not args.path.is_file():
        print(f"Error: File '{args.path}' not found.", file=sys.stderr)
        return 1

    try:
        tasks = load_tasks(args.path)
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    prioritised = sorted(
        tasks,
        key=lambda t: t.importance / t.days_left(args.today),
        reverse=True,
    )

    remaining = args.hours
    plan: list[tuple[str, float]] = []

    for task in prioritised:
        if remaining <= 0:
            break
        allocated = min(task.effort_h, remaining)
        if allocated > 0:
            plan.append((task.title, allocated))
            remaining -= allocated

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, (title, hours) in enumerate(plan, start=1):
        print(f"  {idx}. {title:<14} {hours:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())