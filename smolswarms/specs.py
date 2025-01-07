"""Specifications for agents and business units in the swarm."""

from pydantic import BaseModel


class AgentSpec(BaseModel):
    """Specification for an individual agent in the swarm."""

    name: str
    role: str
    capabilities: list[str]
    memory_size: int = 1024


class BusinessUnit(BaseModel):
    """A business unit that groups agents together for a specific purpose."""

    name: str
    description: str
    agents: list[AgentSpec]
    objectives: list[str]
