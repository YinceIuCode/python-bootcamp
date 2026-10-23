"""Module for loading and saving task data using CSV and JSON formats."""

import csv
import json
from datetime import date
from typing import Any

from .models import Task


def load_tasks(path: str) -> list[Task]:
    """Load tasks from a CSV file.

    Args:
        path: The file path to the CSV file.

    Returns:
        A list of Task objects parsed from the CSV rows.

    Raises:
        ValueError: If a row contains invalid data or formatting.
    """
    tasks: list[Task] = []

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
    """Save a list of tasks to a JSON file.

    Args:
        tasks: A list of Task objects to serialize.
        path: The target file path for the JSON output.
    """
    data: list[dict[str, Any]] = []

    for task in tasks:
        task_dict: dict[str, Any] = {}
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
