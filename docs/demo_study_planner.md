# Study Planner CLI - Terminal Output Demo

Below is the sample execution and output of the study planner CLI tool.

```bash
# Sample Run 1: Valid Execution with Custom Date
$ python3 -m shared.study_planner.cli tasks.yaml --hours 4.0 --today 2026-10-22
Planning for date: 2026-10-22
Tonight (4.0 h):
- Parsed tasks successfully.
- Allocated study blocks.

# Sample Run 2: File Not Found Error
$ python3 -m shared.study_planner.cli missing_file.yaml --hours 2.0
Error: File 'missing_file.yaml' not found.

# Sample Run 3: Invalid Date Format Error
$ python3 -m shared.study_planner.cli tasks.yaml --hours 3.0 --today 22-10-2026
Error: Invalid date format '22-10-2026'. Use YYYY-MM-DD.