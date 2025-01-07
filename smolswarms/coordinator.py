"""
SwarmCoordinator: The raid leader of our agent swarm fr fr.
"""

import json
import os
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

from github import Github
from rich import print
import typer


class SwarmCoordinator:
    def __init__(self) -> None:
        # Using SWARM_TOKEN instead of GITHUB_TOKEN cuz we ain't trying to get ratio'd by GitHub Actions
        self.gh = Github(os.getenv("SWARM_TOKEN"))
        self.memory_path = Path(".memory/swarm.db")
        self.setup_memory()