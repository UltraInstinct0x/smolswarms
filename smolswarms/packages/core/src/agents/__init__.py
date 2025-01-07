"""
Agents module - More autonomous than my coffee machine fr fr 🤖
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class AgentRole(str, Enum):
    RESEARCHER = "researcher"
    ANALYST = "analyst"
    COORDINATOR = "coordinator"
    EXECUTOR = "executor"


class AgentPersonality(str, Enum):
    ZOOMER = "zoomer"
    PROFESSIONAL = "professional"
    CHAOTIC_GOOD = "chaotic_good"


@dataclass
class AgentConfig:
    role: AgentRole
    personality: AgentPersonality
    skills: List[str]
    max_tokens: Optional[int] = 1000
    safety_level: str = "high"


class Agent:
    """Base agent class that hits different fr fr"""

    def __init__(self, config: AgentConfig):
        self.config = config
        self.memory: Dict[str, Any] = {}  # More persistent than my attention span
        self.active = True
        self.vibe_check_status = "passing"

    async def execute_task(self, task: str) -> Dict[str, Any]:
        """Makes the agent do something (more useful than my first Discord bot)"""
        raise NotImplementedError("Subclasses must implement execute_task")

    async def communicate(
        self, message: str, target_agent: Optional["Agent"] = None
    ) -> str:
        """Slides into other agents' DMs"""
        raise NotImplementedError("Subclasses must implement communicate")

    def vibe_check(self) -> str:
        """Checks if agent is acting sus"""
        return self.vibe_check_status
