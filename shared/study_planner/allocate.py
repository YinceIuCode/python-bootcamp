from datetime import date

from shared.contract import Block, Task

# prioritize importantness
def allocate(tasks: list[Task], hours: float) -> list[Block]:
    tasks.sort(key=lambda h : h.effort_h)
    
    block_return = []
    
    for task in tasks:
        if task.effort_h <= hours:
            block_return.append(Block(task, task.effort_h))
            hours -= task.effort_h

    return block_return

task_1 = Task("Huge Task", 5, 10.0, date(2026, 10, 30))
task_2 = Task("Test_2", 4, 5, date(2020, 10, 4))
task_3 = Task("Test_3", 1, 3, date(2020, 10, 6))

print(allocate([task_1, task_2, task_3], 8))
