import csv
import json
from datetime import datetime, date
from pathlib import Path
from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file with header: title,importance,effort_h,deadline."""
    tasks = []
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)

        for line_num, row in enumerate(reader, start=2):
            if not row or all(field.strip() == "" for field in row):
                continue
            try:
                if len(row) < 4:
                    raise ValueError("Missing required columns")

                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = datetime.strptime(row[3].strip(), "%Y-%m-%d").date()

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except Exception as e:
                raise ValueError(f"Error at line {line_num}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save a list of Task objects to a JSON file."""
    path = Path(path)
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.strftime("%Y-%m-%d"),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)