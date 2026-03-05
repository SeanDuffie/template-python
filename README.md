# Modern Python Project Template <!-- omit in toc -->

A professional-grade, high-performance Python template utilizing uv for package management, ruff for linting, and loguru for structured logging. 

This project is structured using the src-layout to ensure clean packaging and testability.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [🛠 Features \& Modern Choices](#-features--modern-choices)
- [📂 Project Structure](#-project-structure)
- [Initial Setup for a New Project](#initial-setup-for-a-new-project)
- [Development Workflow](#development-workflow)
  - [Running the App](#running-the-app)
  - [Linting \& Formatting](#linting--formatting)
  - [Logging](#logging)
  - [🧪 Testing Strategy](#-testing-strategy)
    - [How to Run Tests](#how-to-run-tests)
  - [📦 Building the Executable](#-building-the-executable)
  - [⚙️ VS Code Integration](#️-vs-code-integration)
  - [🛑 Important Notes](#-important-notes)
- [Updating README.md Table Of Contents (TOC)](#updating-readmemd-table-of-contents-toc)
- [TODO](#todo)
  - [Features](#features)
  - [Bugs](#bugs)

## 🛠 Features & Modern Choices
| Feature |	Tool / Choice |	Why? |
| :--- | :--- | :--- |
| Environment |	uv |	100x faster than pip. Manages Python versions and venvs automatically. |
| Structure |	src/ Layout |	Industry standard. Prevents accidental imports and ensures clean builds. |
| Linting/Formatting |	Ruff |	Rust-based; replaces Black, Flake8, and isort with near-instant speed. |
| Logging |	Loguru |	Zero-config, colored terminal output, and automatic file rotation. |
| Secrets |	.env + dotenv |	Keeps API keys out of Git. Loaded at runtime, not baked into binaries. |
| Testing |	pytest |	The standard for Python testing; configured via pyproject.toml. |
| Compilation |	PyInstaller |	Bundles the app into a single .exe with icon and version support. |

## 📂 Project Structure

```my-project/
├── .vscode/                # VS Code settings, launch configurations, and snippets
├── src/                    # All source code lives here
│   └── my_project/         # Primary package (must contain __init__.py)
│       ├── api/            # Placeholder for FastAPI/Web routes
│       ├── cli/            # Placeholder for Typer/Terminal commands
│       ├── data/           # Static assets or data files
│       ├── __init__.py     # Marks the project as a package
│       ├── config.py       # Allows use of secrets
│       ├── logic.py        # Core "engine" (independent of interface)
│       ├── main.py         # App entry point
│       ├── models.py       # Define Data structures
│       └── utils.py        # Define auxiliary functions
├── tests/                  # Pytest unit and integration tests
├── .env                    # Local secrets (GIT IGNORED)
├── .env.example            # Template for required secrets
├── .python-version         # Pinned Python version for the project
├── pyproject.toml          # Project metadata and dependency groups
├── uv.lock                 # Deterministic lockfile (COMMIT THIS)
└── main.spec               # PyInstaller build configuration

```

## Initial Setup for a New Project

1. Navigate to the [GitHub Page](https://github.com/SeanDuffie/Python-Template).
2. "Use this template" -> Create a new repository
3. Clone the repo to your development environment, then open the folder as a project in VS Code.
4. Install [uv](https://docs.astral.sh/uv/getting-started/installation) (if not done already)
    1. Windows:
       - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
    2. macOS and Linux:
        - either: `curl -LsSf https://astral.sh/uv/install.sh | sh`
        - or: `wget -qO- https://astral.sh/uv/install.sh | sh`
5. Initialize uv:
``` bash
uv init --package
uv add loguru python-dotenv
uv add --group dev pytest ruff pyinstaller
```
6. Setup Secrets: Copy `.env.example` to `.env` and fill in the values.
7. Sync the Environment:
``` bash
uv sync
```

## Development Workflow

### Running the App

Always run using uv to ensure the virtual environment and PYTHONPATH are handled correctly:
``` bash
uv run python -m my_project.main
```

### Linting & Formatting

Ruff is integrated into VS Code (see .vscode/settings.json), but can be run manually:

``` bash
uv run ruff check .   # Lint
uv run ruff format .  # Format
```

### Logging

Logs are sent to the console (Info level) and logs/app.log (Debug level). The log file automatically rotates at 10MB.

### 🧪 Testing Strategy

This template uses `pytest` for automated testing. Tests are isolated from the core package to ensure that development tools are not bundled into production builds.

#### How to Run Tests
```bash
uv run pytest          # Run all tests
uv run pytest -v       # Run with verbose output (shows function names)
uv run pytest --lf     # Run only the last-failed tests
```


### 📦 Building the Executable

The project is configured to build a single-file executable using PyInstaller.
1. ***Prepare Icons***: Place a .ico file in the root or assets/.
2. ***Update the Spec***: Ensure `main.spec` has the correct pathex=['src'] and icon path.
3. ***Build***:
``` bash
uv run pyinstaller main.spec
```
4. ***Distribution***: The .exe will be in the dist/ folder. Note: The user must place a .env file in the same folder as the .exe to provide required API keys.

### ⚙️ VS Code Integration

We have included a launch.json that:
- Uses the uv virtual environment automatically.
- Loads the .env file for debugging sessions.
- Enables "Just My Code" to keep debugging focused on your logic.

### 🛑 Important Notes

1. ***NEVER*** commit .env or the .venv folder.

2. ***ALWAYS*** commit uv.lock. It ensures everyone on the team has the exact same environment.

3. ***Imports***: Always use absolute imports from the package root (e.g., from my_project.logic import ...).

## Updating README.md Table Of Contents (TOC)

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Select `Markdown All in One: Create Table of Contents` to insert a TOC.
3. It will automatically update every time the file is saved.

## TODO

### Features

TODO

### Bugs

TODO


