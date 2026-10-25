# Python Bootcamp - Team 03

This repository contains the individual exercises and shared team project for the **Python Bootcamp** program (Weeks 1–3). It serves as a central hub for practical coding, automated testing (CI/CD), and tracking team member progress.

---

## 🚀 1. Virtual Environment Setup (`venv`)

To ensure smooth dependency management and prevent conflicts with system-level packages, all team members **must** set up a local virtual environment before coding.

### Step 1: Create the Virtual Environment

Open your terminal or command prompt at the root directory of the repository and run:

* **All Operating Systems:**
```bash
python -m venv venv
```
*(Use `python3 -m venv venv` if your system defaults `python` to Python 2).*

### Step 2: Activate the Virtual Environment
* Windows (Command Prompt):
```DOS
venv\Scripts\activate
```
* Windows (PowerShell):
```PowerShell
venv\Scripts\Activate.ps1
```
*(Note: If you encounter an Execution Policy error on PowerShell, run `Set-ExecutionPolicy Unrestricted -Scope Process` first).*

* macOS / Linux:
```Bash
source venv/bin/activate
```

## 📦 2. Installing Dependencies
After activating your virtual environment (`venv`), upgrade `pip` and install the required testing and linting tools:
```Bash
pip install --upgrade pip
pip install pytest ruff
```

## 🧪 3. Running Local Tests & Linter
Before pushing your changes to GitHub, run tests and linter checks locally to ensure all solutions pass.

**Individual Homework Tests (W1, W2, W3)**
```Bash
pytest -q tests/test_w1.py --member <github_username> --variant <variant_number>
pytest -q tests/test_w2.py --member <github_username> --variant <variant_number>
pytest -q -s tests/test_w3.py --member <github_username> --variant <variant_number>
```
**Example:**
```Bash
pytest -q -s tests/test_w3.py --member YinceIuCode --variant 1
```
**Code Style & Linter Check (ruff)**
```Bash
ruff check .
```

## 📅 4. Shared Study Planner CLI (Team Project W2–W3)
The team project in `shared/study_planner/` provides a complete CLI workflow (`parse_csv -> prioritise -> allocate -> render`) with error handling and execution logging to `study_planner.log`.

**Run the Study Planner CLI**
```Bash
python -m shared.study_planner samples/tasks.csv --hours 2
python -m shared.study_planner samples/tasks.csv --hours 3.0 --today 2026-10-26
```
**Run Team Unit & End-to-End Tests**
```Bash
pytest -q tests/test_parse.py tests/test_prioritise.py tests/test_allocate.py tests/test_render.py
pytest -q -s tests/test_e2e_w3.py
```

## 📝 5. Note on Extended Variants
According to the bootcamp guidelines:

* Variants 1, 2, 3, 4: Mandatory test execution. Code must pass `pytest` locally and pass automated CI checks on GitHub.

* Variants 5, 6, 7: Extended variants that are **EXEMPT FROM AUTOMATED TESTS**.

## 🔄 6. Git Workflow & Commit Guidelines (Quick Reference)

1. Pull the latest main branch:
```Bash
git switch main
git pull origin main
```
2. Create and switch to your feature branch (replace `<N>` with `1`, `2`, or `3`):
```Bash
git switch -c py/w<N>-<github-username>
```
3. Complete your assignments in `members/<username>/w<N>/` or `shared/study_planner/`.

4. Commit work per exercise independently:
```Bash
git add <files>
git commit -m "feat(py-w3): W3-3 implement study planner CLI"
```

5. Push your branch to GitHub:
```Bash
git push -u origin py/w<N>-<github-username>
```
6. **Open a Pull Request (PR)** on GitHub, tag your designated peer reviewer, and await review/approval before merging.