import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for line, row in enumerate(reader, start=2):
            try:
                task = Task(
                    row[0], int(row[1]), float(row[2]), date.fromisoformat(row[3])
                )

                tasks.append(task)

            except Exception as e:
                raise ValueError(f"invalid row at line {line}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = []

    for task in tasks:
        task_dict = {}
        task_dict["title"] = task.title
        task_dict["importance"] = task.importance
        task_dict["effort_h"] = task.effort_h
        task_dict["deadline"] = task.deadline.isoformat()

        data.append(task_dict)

    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)  # who use indent 4 is gay and microslop


if __name__ == "__main__":
    load_tasks("samples/tasks.csv")
    save_json(load_tasks("samples/tasks.csv"), "samples/tasks.json")
