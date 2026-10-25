import csv
from datetime import date

from shared.contract import Task
from shared.study_planner.logger import get_logger

logger = get_logger(__name__)

def parse_csv(path: str) -> list[Task]:
    """Parse tasks from a CSV file and log the reading event."""
    logger.info("Reading tasks from CSV file: %s", path)
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
                logger.error("Invalid row at line %d in %s: %s", line, path, e)
                raise ValueError(f"invalid row at line {line}: {e}") from e

    logger.info("Successfully loaded %d tasks from %s", len(tasks), path)
    return tasks
