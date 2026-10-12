import csv

from models import Task, date


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
    with open(path, "+w") as csvfile:
        if not csvfile.writable():
            raise FileExistsError("Cannot write to file.")
        
        buffer = [["title", "importance", "effort_h", "deadline"]]
        
        for task in tasks:
            buffer.append([f'{task.title}',f'{task.importance}',f'{task.effort_h}',f'{task.deadline.year}-{task.deadline.month}-{task.deadline.day}'])
        
        writeon = csv.writer(csvfile)
        writeon.writerows(buffer)
        
save_json(load_tasks("test.csv"), "output.csv")

    