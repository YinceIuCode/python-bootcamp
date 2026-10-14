from members.doomsdaycome.w2.io_utils import *
from members.doomsdaycome.w2.models import Task


def parse_csv(path: str) -> list[Task]:
    return load_tasks(path)
