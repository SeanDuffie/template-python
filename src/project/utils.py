""" @file utils.py
    @author Sean Duffie
    @brief This file is for code that is used in multiple places but isn't core logic.
"""

import re
from pathlib import Path

def slugify(text: str) -> str:
    """Converts 'Hello World' to 'hello-world' for filenames."""
    return re.sub(r"[\W_]+", "-", text).lower()

def get_project_root() -> Path:
    """Returns the absolute path to the project root directory."""
    return Path(__file__).parent.parent.parent.parent
