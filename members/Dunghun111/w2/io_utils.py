import csv
import json
from dataclasses import asdict

from .models import Task, date


def load_tasks(path) -> list[Task]:
    line_number = 2
    
    with open(path, "r", newline="") as csvfile:
        info_list = [*csv.reader(csvfile)][1:]
        task_list = []
        
        try:
            for info in info_list:
                if len(info) != 4 or ('' in info): 
                    raise ValueError
                                
                info_date = date(*map(int, info[3].split("-")))
                task_list.append(Task(info[0], int(info[1]), float(info[2]), info_date))
                line_number += 1
            
            return task_list
                
        except (ValueError, TypeError):
            raise ValueError(f"Invalid task at line {line_number}")
        
    
def save_json(tasks : list[Task], path: str):
    with open(path, "+w") as jsonfile:
        if not jsonfile.writable():
            raise FileExistsError("Cannot write to file.")
        
        list_task_dict = []
        for task in tasks:
            list_task_dict.append(asdict(task))
            
        json.dump(list_task_dict, jsonfile, default=str)
        

save_json(load_tasks("samples/tasks.csv"), "tasks.json")
