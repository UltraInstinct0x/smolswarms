"""
Factory module - Spawning agents like they're Minecraft villagers fr fr 🏭
"""

from dataclasses import dataclass
from typing import List, Optional

from .agents import Agent, AgentConfig, AgentPersonality, AgentRole
from .memory import InMemoryStore, MemoryManager
from .swarm import Swarm, SwarmConfig, SwarmStrategy


@dataclass
class FactoryConfig:
    api_key: str
    max_agents: int = 10
    safety_level: str = "high"
    memory_type: str = "in_memory"
    default_personality: AgentPersonality = AgentPersonality.ZOOMER


class SwarmFactory:
    """The blessed way to spawn your agents"""

    def __init__(self, config: FactoryConfig):
        self.config = config
        self.active_agents: List[Agent] = []
        self.memory_manager = MemoryManager(InMemoryStore())

    def create_agent(
        self,
        role: AgentRole,
        personality: Optional[AgentPersonality] = None,
        skills: Optional[List[str]] = None,
    ) -> Agent:
        """Spawns a single agent (more useful than my first Discord bot)"""
        if len(self.active_agents) >= self.config.max_agents:
            raise ValueError("Too many agents fr fr, touch grass")

        agent_config = AgentConfig(
            role=role,
            personality=personality or self.config.default_personality,
            skills=skills or ["python", "vibing"],
            safety_level=self.config.safety_level,
        )

        agent = Agent(agent_config)
        self.active_agents.append(agent)
        return agent

    def create_swarm(
        self,
        size: int,
        strategy: SwarmStrategy = SwarmStrategy.COLLABORATIVE,
        roles: Optional[List[AgentRole]] = None,
    ) -> Swarm:
        """Spawns multiple agents (like a Discord raid but legal)"""
        if size > self.config.max_agents:
            raise ValueError("Trying to spawn too many agents fr fr")

        swarm_config = SwarmConfig(size=size, strategy=strategy, safety_checks=True)

        swarm = Swarm(swarm_config)

        # Create and add agents to the swarm
        for i in range(size):
            role = roles[i] if roles and i < len(roles) else AgentRole.RESEARCHER
            agent = self.create_agent(role=role)
            swarm.add_agent(agent)

        return swarm

    def get_agent_count(self) -> int:
        """How many agents you've spawned (touch grass if too high)"""
        return len(self.active_agents)
