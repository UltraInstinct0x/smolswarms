"""
Data models and schemas for smolswarms.

This module contains Pydantic models for:
- AgentConfig: Configuration for individual agents
- SwarmConfig: Configuration for entire swarms
- TaskSpec: Task specification and requirements
- MetricsData: Performance and usage metrics
"""

from pydantic import BaseModel


class BaseConfig(BaseModel):
    """Base configuration model."""

    name: str
    description: str
