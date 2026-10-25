from datetime import date

from shared.contract import Block, Task

# prioritize importantness
def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate tasks into hour blocks"""
    tasks.sort(key=lambda h : h.effort_h)
    
    block_return = []
    
    for task in tasks:
        if task.effort_h <= hours:
            block_return.append(Block(task, task.effort_h))
            hours -= task.effort_h

    return block_return