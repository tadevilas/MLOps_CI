# MLOps_CI
This Repo is for Continuous Integration 

# 🚀 CI Workflow for Python Project

This repository demonstrates a basic **Continuous Integration (CI)** pipeline using **GitHub Actions** for a Python project. The workflow is triggered on every push and pull request to the `main` branch and automatically runs tests using `pytest`.

---

## 🔧 What the Workflow Does

- **Triggers on Code Changes:** Automatically runs when you push code or open a pull request targeting the `main` branch.
- **Checks Out Your Code:** Uses GitHub Actions to pull the latest code from the repository.
- **Sets Up Python:** Configures Python 3.9 in the GitHub-hosted runner.
- **Installs Dependencies:** Installs `pytest`, `streamlit`, and upgrades `pip`.
- **Runs Unit Tests:** Executes a test script (e.g., `_test.py`) using `pytest`.

---

## 📁 Project Structure

Typical files in this project may include:

- `.github/workflows/ci.yml` – GitHub Actions workflow file
- `_test.py` – Unit tests written with `pytest`
- `main.py` or similar – Your actual application logic
- `README.md` – Project documentation

---

## ✅ Getting Started Locally

To run the same tests locally:

1. Ensure Python 3.9+ is installed.
2. Install required dependencies:
   ```bash
   pip install pytest streamlit
ss