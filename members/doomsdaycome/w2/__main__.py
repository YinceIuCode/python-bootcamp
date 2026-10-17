from pathlib import Path

from .errors import InfeasiblePlan
from .io_utils import load_tasks, save_json


def main():
    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    csv_path = base_dir / "samples" / "tasks.csv"
    tmp_dir = base_dir / "members" / "doomsdaycome" / "w2" / "temp"

    tmp_dir.mkdir(parents=True, exist_ok=True)

    tmp_path = tmp_dir / "tasks.json"

    try:
        tasks = load_tasks(str(csv_path))
        save_json(tasks, str(tmp_path))

        with open(tmp_path, mode="r", encoding="utf-8") as file:
            print(file.read())

    except (FileNotFoundError, ValueError, InfeasiblePlan) as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
