import csv
import json
from dataclasses import asdict
from datetime import date 
from models import Task

def load_task(path: str) -> list[Task]:
    list_of_tasks = []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)   # return list[str]
        next(reader)                # pass the header row

        for line_num, row in enumerate(reader, start = 2):      # start at line 2     
            if not row:     # pass blank rows
                continue      

            try:
                if (len(row) != 4):
                    raise ValueError("Row does not have exactly 4 columns")
                
                title = row[0]
                importance = int(row[1])
                effort_h = float(row[2])
                deadline = date.fromisoformat(row[3])

                task = Task(title, importance, effort_h, deadline)
                list_of_tasks.append(task)

            except(ValueError, IndexError) as error:
                raise ValueError(f"Invalid data at line {line_num}: {error}") from error
    return list_of_tasks

def save_json(tasks: list[Task], path: str):
    data = [asdict(task) for task in tasks]     # asdict function: change Task -> dict

    with open(path, mode = "w", encoding= "utf-8") as file:
        json.dump(data, file, indent= 4, default=str)