import csv
import json
from datetime import datetime

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Bỏ qua dòng header

        for line_num, row in enumerate(reader, start=2):
            if not row or all(field.strip() == "" for field in row):
                continue
            if len(row) < 4:
                raise ValueError(f"line {line_num}: Invalid number of fields.")

            try:
                title = row[0].strip()
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = datetime.strptime(
                    row[3].strip(), "%Y-%m-%d"
                ).date()

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except Exception as e:  # noqa: BLE001
                raise ValueError(f"line {line_num}: {e}")

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)