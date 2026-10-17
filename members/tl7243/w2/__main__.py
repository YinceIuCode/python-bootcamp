from pathlib import Path

from .io_utils import load_tasks


def main():
	sample_dir = Path(__file__).parents[3] / "samples"
#	csv2 = sample_dir / "tasks_bad.csv"
#	tasks = load_tasks(str(csv2))
	csv = sample_dir / "tasks.csv"
	tasks = load_tasks(str(csv))

	for task in tasks:
		print(task)

#	save_json(tasks, str(sample_dir) + "/tasks.json")

#	check_feasible(tasks,7)

if __name__ == "__main__":
	main()
