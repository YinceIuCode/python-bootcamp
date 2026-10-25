import argparse
import sys
from datetime import date

from shared.study_planner import allocate

from ..w2.io_utils import load_tasks


def main():
    """CLI Application for study planner"""
    prog = argparse.ArgumentParser(
        "Study Planer", 
        description="CLI for study planner", 
        add_help=True,
    )

    prog.add_argument("file", type=str, help="File")
    prog.add_argument("--today", nargs = "*", help="Today")
    prog.add_argument("--hours", nargs = 1, help="Hours.")

    try:
        args = prog.parse_args()

    except SystemExit:
        return 1
    
    file_path : str
    hours : float

    if args.file:
        file_path = args.file
        if file_path == "":
            return 1
        
        try:
            with open(file_path, "r"):
                ...
        
        except (FileExistsError, FileNotFoundError):
            return 1
    
    if args.hours:
        hours = float(*args.hours)
        
        if hours < 0:
            return 1  
    
    if args.today:
        if len(args.today[0].split("-")) != 3:
            return 1
        
        try:
            date(int(args.today[0].split("-")[0]), int(args.today[0].split("-")[1]), int(args.today[0].split("-")[2]))
            
        except ValueError:
            return 1
        
    tasks_parsed = load_tasks(file_path)
    hours_blocks = allocate.allocate(tasks_parsed, hours)

    hours_blocks.sort(key = lambda k : len(k.task.title), reverse=True)
    
    total_hours_allocated = 0
    for block in hours_blocks:
        total_hours_allocated += block.hours
    
    print(f"Tonight ({total_hours_allocated} h)")
    
    max_length = -1
    for block_index in range(len(hours_blocks)):
        block = hours_blocks[block_index]
        
        max_length = max(max_length, len(block.task.title))
            
        print(f"  {block_index}. {block.task.title} " + (6 + (max_length - len(block.task.title))) * "." + f" {block.hours} h")

    return 0

if __name__ == "__main__":
    sys.exit(main())