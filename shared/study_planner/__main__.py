import argparse
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.errors import InfeasiblePlan, check_feasible
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
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
    
    try:
        tasks = parse_csv(parsed_args.filename)

        if len(tasks) == 0:
            print("Parse error: Empty task in csv.")
            return
        
    except FileExistsError:
        print("File error: File is empty/invalid.")
        return

    except FileNotFoundError:
        print("File error: Cannot found file.")
        return
    
    prioritized_tasks = prioritise(tasks, parsed_args.today)
    
    try:
        check_feasible(prioritized_tasks, parsed_args.hours)
    
    except InfeasiblePlan:
        print("Plan warning: Plan is not feasible. Some tasks will be discarded to satisfy available hour(s).")
        
    plan = allocate(prioritized_tasks, parsed_args.hours)
    print(render(plan))


if __name__ == "__main__":
    main()