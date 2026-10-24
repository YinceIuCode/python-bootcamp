from shared.contract import Block, Task
from shared.study_planner.logger import get_logger

logger = get_logger(__name__)


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Allocate study blocks greedily within available hours."""
    allocated_blocks: list[Block] = []
    available_hours = hours
    
    for task in tasks:
        if available_hours >= task.effort_h:
            allocated_blocks.append(Block(task, task.effort_h))
            available_hours -= task.effort_h

    logger.info(
        "Allocation complete: %d/%d tasks scheduled (%.1fh remaining).",
        len(allocated_blocks),
        len(tasks),
        available_hours,
    )        
    return allocated_blocks