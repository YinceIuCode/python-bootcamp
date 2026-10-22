"""Command-line interface tool for study planner task allocation."""

import argparse
import sys
from datetime import date
from pathlib import Path


def main() -> None:
    """Execute the CLI application to parse arguments and display study schedule."""
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

    print(f"Planning for date: {today_date.isoformat()}")
    print(f"Tonight ({args.hours:.1f} h):")


if __name__ == "__main__":
    main()