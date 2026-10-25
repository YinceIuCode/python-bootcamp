# Study Planner System

A lightweight command-line tool designed to parse tasks from a CSV file, prioritise them by importance and deadline, and greedily allocate study blocks within available hours.

## 🚀 Installation & Requirements

Ensure you have **Python 3.10+** installed on your system. No external dependencies are required beyond the Python Standard Library (`argparse`, `csv`, `datetime`, `logging`, `pathlib`).

## 📖 Sample CLI Execution Commands

Run the commands below from the `python-bootcamp/` directory:

### 1. Basic Task Allocation
Execute with the sample tasks CSV file and total available hours:
```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

### 2. Custom Anchor Date
Specify an anchor date (`--today`) in `YYYY-MM-DD` format for priority calculation:
```bash
python -m shared.study_planner samples/tasks.csv --hours 3.0 --today 2026-10-26
```

### 3. View CLI Help
```bash
python -m shared.study_planner --help
```

### 📋 Sample Output
```Plaintext
Plan warning: Plan is not feasible. Some tasks will be discarded to satisfy available hour(s).
=== Study Planner Blocks ===
1. Task: Assignment | Importance: 4 | Deadline: 2026-10-27 | Allocated: 1.5h
Total Allocated Hours: 1.5h
```