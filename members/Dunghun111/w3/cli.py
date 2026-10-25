import argparse
from datetime import date
from shared.study_planner import allocate, parse

if __name__ == "__main__":
    prog = argparse.ArgumentParser(
        "Study Planer", 
        description="CLI for study planner", 
        add_help=True,
    )

    prog.add_argument("file", type=str, help="File")
    prog.add_argument("--today", nargs = "*", help="Today")
    prog.add_argument("--hours", nargs = 1, help="Hours.")


    args = prog.parse_args()

    file_path : str
    hours : float
    today_str : list[str]

    if args.file:
        file_path = args.file
    
    if args.hours:
        hours = float(*args.hours)
        
    if args.today:
        today_str = args.today[0].split("-")
    
    
    today = date(int(today_str[0]), int(today_str[1]), int(today_str[2]))
    
    tasks_parsed = parse.parse_csv(file_path)
    hours_blocks = allocate.allocate(tasks_parsed, hours)

    hours_blocks.sort(key = lambda k : len(k.task.title), reverse=True)
    
    total_hours_allocated = 0
    for block in hours_blocks:
        total_hours_allocated += block.hours
    
    print(f"Tonight ({total_hours_allocated} h)")
    
    max_length = -1
    for block_index in range(len(hours_blocks)):
        block = hours_blocks[block_index]
        
        if len(block.task.title) > max_length:
            max_length = len(block.task.title)
            
        print(f"  {block_index}. {block.task.title} " + (6 + (max_length - len(block.task.title))) * "." + f" {block.hours} h")