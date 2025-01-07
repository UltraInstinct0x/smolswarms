"""Tests for the Swarm class."""

from smolswarms.factory import SwarmFactory
from smolswarms.specs import AgentSpec
from smolswarms.specs import BusinessUnit


def test_swarm_creation() -> None:
    """Test creating a swarm."""
    swarm = SwarmFactory.create_swarm("test_swarm", "A test swarm")
    assert swarm.name == "test_swarm"
    assert swarm.description == "A test swarm"
    assert len(swarm.business_units) == 0
    assert len(swarm.agents) == 0


def test_business_unit_addition() -> None:
    """Test adding a business unit to a swarm."""
    swarm = SwarmFactory.create_swarm("test_swarm")
    agent = AgentSpec(
        name="test_agent",
        role="tester",
        capabilities=["testing"],
    )
    unit = BusinessUnit(
        name="test_unit",
        description="A test unit",
        agents=[agent],
        objectives=["test everything"],
    )
    swarm.add_business_unit(unit)
    assert len(swarm.business_units) == 1
    assert len(swarm.agents) == 1
    assert swarm.get_agent("test_agent") == agent


def test_agent_retrieval() -> None:
    """Test retrieving agents from a swarm."""
    swarm = SwarmFactory.create_swarm("test_swarm")
    agent1 = AgentSpec(
        name="agent1",
        role="role1",
        capabilities=["cap1"],
    )
    agent2 = AgentSpec(
        name="agent2",
        role="role2",
        capabilities=["cap2"],
    )
    unit = BusinessUnit(
        name="test_unit",
        description="A test unit",
        agents=[agent1, agent2],
        objectives=["objective"],
    )
    swarm.add_business_unit(unit)

    found_agent = swarm.get_agent("agent1")
    assert found_agent == agent1
    assert swarm.get_agent("nonexistent") is None
