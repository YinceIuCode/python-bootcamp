
from shared.contract import Block


def render(blocks: list[Block]) -> str:
    """Render a list of study/work blocks into a readable string format."""
    if not blocks:
        return "No blocks to render."

    lines = ["=== Study Planner Blocks ==="]
    total_hours = 0.0

    for i, b in enumerate(blocks, start=1):
        task_title = b.task.title
        importance = b.task.importance
        deadline = b.task.deadline
        hours = b.hours
        total_hours += hours

        line = (
            f"{i}. Task: {task_title} | Importance: {importance} "
            f"| Deadline: {deadline} | Allocated: {hours}h"
        )
        lines.append(line)

    lines.append(f"Total Allocated Hours: {total_hours}h")
    return "\n".join(lines)