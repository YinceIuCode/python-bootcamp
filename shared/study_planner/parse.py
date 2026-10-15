import csv
from datetime import date

from shared.contract import Task


def parse_csv(path: str) -> list[Task]:
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
