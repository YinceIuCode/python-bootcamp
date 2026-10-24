from shared.contract import Block, Task

def allocate(tasks: list[Task], hours: float) -> list[Block]:
    allocated_blocks = []
    available_hours = hours
    
    for task in tasks:
        if available_hours >= task.effort_h:
            allocated_blocks.append(Block(task, task.effort_h))
            available_hours -= task.effort_h
            
    return allocated_blocks