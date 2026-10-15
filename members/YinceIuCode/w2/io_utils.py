import csv
import json
from datetime import datetime

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """Reads a CSV file and returns a list of Task objects."""
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):  # Dòng 1 là header
            try:
                title = row["title"].strip()
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                # Chuyển chuỗi YYYY-MM-DD thành kiểu date
                deadline = datetime.strptime(row["deadline"].strip(), "%Y-%m-%d").date()

                task = Task(
                    title=title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except (KeyError, ValueError) as e:
                raise ValueError(f"Invalid data at line {line_num} in {path}: {e}")
    return tasks


def save_json(tasks: list[Task], path: str):
    """Saves a list of Task objects to a JSON file."""
    data = []
    for t in tasks:
        data.append(
            {
                "title": t.title,
                "importance": t.importance,
                "effort_h": t.effort_h,
                "deadline": t.deadline.isoformat(),
            }
        )
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
