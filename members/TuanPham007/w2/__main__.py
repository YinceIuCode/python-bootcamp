from pathlib import Path
from .io_utils import load_tasks


def main() -> None:
    sample_csv = Path(__file__).parent / "sample.csv"

    if not sample_csv.exists():
        sample_csv.write_text(
            "title,importance,effort_h,deadline\n"
            "DS exam,5,6.0,2026-10-30\n"
            "Assignment,4,1.5,2026-10-27\n",
            encoding="utf-8",
        )

    tasks = load_tasks(sample_csv)
    print(f"Loaded {len(tasks)} tasks from {sample_csv.name}:\n")
    for task in tasks:
        print(
            f"- {task.title} (Importance: {task.importance}, "
            f"Effort: {task.effort_h}h, Due: {task.deadline})"
        )


if __name__ == "__main__":
    main()