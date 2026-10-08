# Python Bootcamp - Team 03

This repository contains the exercises and tasks for the **Python Bootcamp** program. It serves as a central hub for practical coding, automated testing (CI/CD), and tracking individual team member progress.

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

* **Windows (Command Prompt):**

  ```cmd
  venv\Scripts\activate
  ```

* **Windows (PowerShell):**

  ```powershell
  venv\Scripts\Activate.ps1
  ```

  *(Note: If you encounter an Execution Policy error on PowerShell, run `Set-ExecutionPolicy Unrestricted -Scope Process` first).*

* **macOS / Linux:**

  ```bash
  source venv/bin/activate
  ```

*(Tip: Upon successful activation, you will see a `(venv)` prefix in your terminal prompt).*

---

## 📦 2. Installing Dependencies

After activating your virtual environment `(venv)`, upgrade `pip` and install the required testing and linting tools:

```bash
pip install --upgrade pip
pip install pytest ruff
```

---

## 🧪 3. Running Local Tests

Before pushing your changes to GitHub, you **MUST** run tests locally to ensure all individual solutions pass.

### Standard Test Command:

```bash
pytest -q tests/test_w1.py --member <your_member_folder> --variant <variant_number>
```

**Parameters:**

* `--member`: Name of your individual directory inside `members/` (e.g., `hoang_duc_vinh`).
* `--variant`: Assign variant number for **W1-4** (Integer from `1` to `7`).

**Example:**

```bash
pytest -q tests/test_w1.py --member hoang_duc_vinh --variant 1
```

---

## 📌 4. Note on Extended Variants (Task W1-4)

According to the bootcamp guidelines:

* **Variants 1, 2, 3, 4:** Mandatory test execution. Code must pass `pytest` locally and pass automated CI checks on GitHub.
* **Variants 5, 6, 7:** Extended variants that are **EXEMPT FROM AUTOMATED TESTS**. If you are assigned variants 5, 6, or 7, local/CI test passing for W1-4 is not required.

---

## 🔄 5. Git Workflow & Commit Guidelines (Quick Reference)

To ensure full contribution points, follow this exact workflow:

1. **Pull the latest `main` branch:**

   ```bash
   git checkout main
   git pull origin main
   ```

2. **Create and switch to your personal feature branch:**

   ```bash
   git switch -c py/w1-<github-username>
   ```

3. **Complete your assignments** in your personal folder: `members/<username>/w1/`.

4. **Commit work per exercise independently** (Minimum 5 commits per week required):

   ```bash
   git add .
   git commit -m "feat (py-w1): W1-2 word counter"
   ```

5. **Push your branch to GitHub:**

   ```bash
   git push -u origin py/w1-<github-username>
   ```

6. **Open a Pull Request (PR)** on GitHub, tag your designated peer reviewer, and await review/approval from the Team Leader.