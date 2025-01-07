"""Tests for the SwarmFactory class."""

from smolswarms.factory import SwarmFactory


def test_create_agent() -> None:
    """Test creating an agent."""
    agent = SwarmFactory.create_agent(
        name="test_agent",
        role="tester",
        capabilities=["testing", "debugging"],
    )
    assert agent.name == "test_agent"
    assert agent.role == "tester"
    assert agent.capabilities == ["testing", "debugging"]
    assert agent.memory_size == 1024  # default value


def test_create_agent_with_memory() -> None:
    """Test creating an agent with custom memory size."""
    agent = SwarmFactory.create_agent(
        name="test_agent",
        role="tester",
        capabilities=["testing"],
        memory_size=2048,
    )
    assert agent.memory_size == 2048


def test_create_business_unit() -> None:
    """Test creating a business unit."""
    unit = SwarmFactory.create_business_unit(
        name="test_unit",
        description="A test unit",
        objectives=["test", "debug"],
    )
    assert unit.name == "test_unit"
    assert unit.description == "A test unit"
    assert unit.objectives == ["test", "debug"]
    assert len(unit.agents) == 0  # starts empty
