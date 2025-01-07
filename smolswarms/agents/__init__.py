"""
Agent implementations for smolswarms.

This module contains different types of agents that can be spawned in a swarm:
- BaseAgent: Abstract base class for all agents
- ResearchAgent: For data analysis and research tasks
- ExecutorAgent: For task execution and coordination
- ReviewerAgent: For code and content review
"""

from typing import Protocol


class Agent(Protocol):
    """Base protocol for all agents in the system."""

    def execute_task(self, task: str) -> None:
        """Execute a given task."""
        ...
