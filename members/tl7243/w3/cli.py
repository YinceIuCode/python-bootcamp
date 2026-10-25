import argparse
import csv
import sys
from datetime import date
from pathlib import Path


def main() -> None:

	"""Run the CLI for study planner tool"""

	parser = argparse.ArgumentParser(description="Tool for planning studies")
	parser.add_argument(
		"tasks_file",
		type=str,
		help="Path to tasks CSV file"
	)
	parser.add_argument(
		"--hours",
		type=float,
		required=True,
		help="Available hours"
	)
	parser.add_argument(
		"--today",
		type=str,
		default=date.today(),
		help="Date in ISO format (YYYY-MM-DD)",
	)
	args = parser.parse_args()

	if args.today:
		try:
			date.fromisoformat(args.today)
		except ValueError:
			print(f"Error: Invalid date format '{args.today}'", file=sys.stderr)
			sys.exit(1)
	else:
		date.today()

	file_path = Path(args.tasks_file)
	if not file_path.exists():
		print(f"Error: File '{args.tasks_file}' not found.", file=sys.stderr)
		sys.exit(1)

	task_list = []
	with open(file_path, mode="r", encoding="utf-8") as f:
		reader = csv.reader(f)
		next(reader)
		for line_num, row in enumerate(reader, start=2):
			if not row:
				continue
			try:
				if(len(row) != 4):
					raise ValueError("Missing CSV fields")
				task_list.append([row[0],int(row[1]),float(row[2]),date.fromisoformat(row[3])])
			except(ValueError, IndexError) as error:
				raise ValueError(f"Line {line_num}: {error}") from error

	task_list=sorted(task_list, key=lambda k: k[1])
	hours = args.hours
	print(f"Tonight ({hours} h):")
	for i in range(len(task_list)):
		print(f"{i+1}. {task_list[i][0]}: {min(hours,task_list[i][2])} h")
		hours = max(0, hours - task_list[i][2])

if __name__ == "__main__":
	main()
