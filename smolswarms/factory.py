"""Factory for creating and configuring swarms."""

from typing import Optional

from .specs import AgentSpec
from .specs import BusinessUnit
from .swarm import Swarm


class SwarmFactory:
    """Factory class for creating and configuring swarms."""

    @staticmethod
    def create_swarm(name: str, description: Optional[str] = None) -> Swarm:
        """Create a new swarm with the given name and description."""
        return Swarm(name=name, description=description)

    @staticmethod
    def create_business_unit(
        name: str, description: str, objectives: list[str]
    ) -> BusinessUnit:
        """Create a new business unit with the given specifications."""
        return BusinessUnit(
            name=name,
            description=description,
            agents=[],
            objectives=objectives,
        )

    @staticmethod
    def create_agent(
        name: str,
        role: str,
        capabilities: list[str],
        memory_size: Optional[int] = None,
    ) -> AgentSpec:
        """Create a new agent with the given specifications."""
        return AgentSpec(
            name=name,
            role=role,
            capabilities=capabilities,
            memory_size=memory_size if memory_size is not None else 1024,
        )
