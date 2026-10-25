import argparse

from shared.study_planner import allocate, parse


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

    args = prog.parse_args()

    file_path : str
    hours : float

    if args.file:
        file_path = args.file
    
    if args.hours:
        hours = float(*args.hours)    
        
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
        
        max_length = max(max_length, len(block.task.title))
            
        print(f"  {block_index}. {block.task.title} " + (6 + (max_length - len(block.task.title))) * "." + f" {block.hours} h")


if __name__ == "__main__":
    main()