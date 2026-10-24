import argparse
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritize import prioritize
from shared.study_planner.render import render


def main(args: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("filename", type=Path, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=date.today(),
        help="Anchor date in YYYY-MM-DD format (default: today)",
    )

    parsed_args = parser.parse_args(args)

    tasks = parse_csv(parsed_args.filename)
    prioritized_tasks = prioritize(tasks, parsed_args.today)
    plan = allocate(prioritized_tasks, [parsed_args.hours])
    print(render(plan))


if __name__ == "__main__":
    main()