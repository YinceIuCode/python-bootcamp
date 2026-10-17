import csv
import json
from datetime import date

from .models import Task


def load_tasks(path: str) -> list[Task]:
	tasks = []
	with open(path, mode="r", encoding="utf-8") as f:
		reader = csv.reader(f)
		next(reader, None)

		for line, row in enumerate(reader, start=2):
			try:
				task = Task(
					row[0].strip(), #title
					int(row[1].strip()), #importance
					float(row[2].strip()), #effort_h
					date.fromisoformat(row[3].strip()) #deadline
				)
				tasks.append(task)
			except (KeyError, ValueError) as e:
				raise ValueError(f"line {line}: {e}")

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
