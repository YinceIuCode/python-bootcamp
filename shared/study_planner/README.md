# Study Planner System

A lightweight command-line tool designed to parse tasks, manage study allocations, and analyze log statistics efficiently.

## 🚀 Installation & Requirements

Ensure you have **Python 3.9+** installed on your system. No external dependencies are required beyond the Python Standard Library (`argparse`, `datetime`, `pathlib`, `collections`).

## 📖 Sample CLI Execution Commands

Below are example commands to run and execute the Study Planner CLI tool in various scenarios:

### 1. Basic Task Allocation
Execute with a tasks file and total allocated hours:
```bash
python3 -m shared.study_planner.cli tasks.yaml --hours 4.5
python3 -m shared.study_planner.cli tasks.yaml --hours 3.0 --today 2026-10-30
python3 -m shared.study_planner.cli --help