"""SwarmCoordinator: The raid leader of our agent swarm fr fr."""

import os
from pathlib import Path

from github import Github


class SwarmCoordinator:
    def __init__(self) -> None:
        """Initialize the coordinator like it's spawning into a new universe."""
        self.gh = Github(os.getenv("SWARM_TOKEN"))
        self.memory_path = Path(".memory/swarm.db")
        self.setup_memory()

    def setup_memory(self) -> None:
        """Set up that persistent memory storage no cap."""
        self.memory_path.parent.mkdir(exist_ok=True)