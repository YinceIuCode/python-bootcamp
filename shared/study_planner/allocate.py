from dataclasses import dataclass
from datetime import date
 
def bisect(find, array):
    s = 0
    e = len(array) - 1
    r : int
    
    while s <= e:
        m = (s + e) // 2

        if array[m] < find:
            s = m  + 1
        
        else:
            r = m
            e = m - 1
    
    return array[r]

# prioritize importantness
def allocate(tasks: list[Task], hours: list[float]) -> list[Block]:
    tasks.sort(key=lambda h : h.importance, reverse=True)
    hours.sort()
    
    hours_map = {h: 0 for h in hours}
    block_return = []
    
    for task in tasks:
        hour = bisect(task.effort_h, hours)
        
        if hour >= task.effort_h and hours_map.get(hour) == 0:
            hours_map[hour] = 1
            block_return.append(Block(task, hour))
    
    return block_return

task_1 = Task("Test_1", 3, 2, date(2020, 10, 3))
task_2 = Task("Test_2", 4, 5, date(2020, 10, 4))
task_3 = Task("Test_3", 1, 3, date(2020, 10, 6))

print(allocate([task_1, task_2, task_3], [1, 3, 6]))
