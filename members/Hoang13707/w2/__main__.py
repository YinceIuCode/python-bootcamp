import os

from .io_utils import load_tasks


def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "sample.csv")

    if not os.path.exists(csv_path):
        with open(csv_path, "w", encoding="utf-8") as f:
            f.write("title,importance,effort_h,deadline\nDS exam,5,6,2026-10-30\nAssignment,4,1.5,2026-10-27\n")

    tasks = load_tasks(csv_path)
    print("Loaded tasks:")
    for t in tasks:
        print(t)

if __name__ == "__main__":
    main()