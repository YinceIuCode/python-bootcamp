import sys
from pathlib import Path
from .io_utils import load_tasks

def main():
    csv_path = Path(__file__).parents[3] / "samples" / "tasks.csv"
    
    if not csv_path.exists():
        print(f"Error: {csv_path} does not exist. Please create a sample CSV.")
        sys.exit(1)

    try:
        tasks = load_tasks(str(csv_path))
        print(f"Loaded {len(tasks)} tasks successfully:")
        for t in tasks:
            print(f"- {t.title} (Importance: {t.importance}, Effort: {t.effort_h}h, Deadline: {t.deadline})")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()