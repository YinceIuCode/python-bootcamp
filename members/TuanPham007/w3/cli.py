import argparse
import sys
from datetime import date, datetime


def main() -> None:
    """Run the main command line interface for the study planner tool."""
    parser = argparse.ArgumentParser(description="Study planner CLI tool.")
    parser.add_argument("file_path", type=str, help="Path to tasks CSV file")
    parser.add_argument(
        "--hours", type=float, required=True, help="Available study hours"
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Date string YYYY-MM-DD (default: today)",
    )

    args: argparse.Namespace = parser.parse_args()

    today_date: date
    if args.today:
        try:
            today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
        except ValueError:
            print(
                f"Error: Invalid date format for --today: {args.today}. Use YYYY-MM-DD.",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        today_date = date.today()

    try:
        with open(args.file_path, "r", encoding="utf-8") as f:
            lines: list[str] = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Tonight ({args.hours:.1f} h, date: {today_date}):")
    task_count: int = 0
    for line in lines[1:]:
        parts: list[str] = [p.strip() for p in line.split(",") if p.strip()]
        if len(parts) >= 2:
            task_count += 1
            task_name: str = parts[0]
            duration: str = parts[1]
            print(f" {task_count}. {task_name:<15} ......... {duration} h")


if __name__ == "__main__":
    main()