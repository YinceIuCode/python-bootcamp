from pathlib import Path

from .io_utils import load_tasks


def main():
    csv_path = Path(__file__).parent / "tasks_bad.csv"
    tasks = load_tasks(str(csv_path))
    
    print(f"Loaded {len(tasks)} tasks:")
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()