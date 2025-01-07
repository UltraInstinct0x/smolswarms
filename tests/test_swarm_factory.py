"""Tests for SwarmFactory."""

from smolswarms.swarm_factory import SwarmFactory


def test_spawn_department() -> None:
    """Test spawning a department."""
    factory = SwarmFactory()
    swarm = factory.spawn_department(
        {
            "business_unit": "growth_team",
            "budget": "optimize_tokens",
            "vibe": "hypergrowth",
        }
    )
    assert swarm is None


def test_spawn_department_with_different_budget() -> None:
    """Test spawning a department with a different budget."""
    factory = SwarmFactory()
    swarm = factory.spawn_department(
        {
            "business_unit": "growth_team",
            "budget": "unlimited",
            "vibe": "hypergrowth",
        }
    )
    assert swarm is None
