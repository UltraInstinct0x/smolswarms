"""Core swarm implementation for orchestrating agents."""

from typing import Optional

from .specs import AgentSpec
from .specs import BusinessUnit


class Swarm:
    """A swarm of agents working together to achieve objectives."""

    def __init__(self, name: str, description: Optional[str] = None) -> None:
        """Initialize a new swarm with a name and optional description."""
        self.name = name
        self.description = description
        self.business_units: list[BusinessUnit] = []
        self.agents: list[AgentSpec] = []

    def add_business_unit(self, unit: BusinessUnit) -> None:
        """Add a business unit to the swarm."""
        self.business_units.append(unit)
        self.agents.extend(unit.agents)

    def get_agent(self, name: str) -> Optional[AgentSpec]:
        """Get an agent by name."""
        for agent in self.agents:
            if agent.name == name:
                return agent
        return None
