---
layout: default
title: SwarmFactory
parent: Reference
nav_order: 1
---

# SwarmFactory
{: .no_toc }

The SwarmFactory do be spawning agents like it's running a quantum gacha game fr fr 🎮
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The `SwarmFactory` is like that one friend who can organize a Discord raid in 0.002 seconds - but for AI agents. It's the main interface for spawning and managing agent swarms that go brr.

```python
from smolswarms import SwarmFactory

factory = SwarmFactory(
    compute_mode="quantum_gaming_chair",  # For that extra performance boost
    budget="more_reasonable_than_my_coffee_spending"
)
```

## Methods

### spawn_department

```python
def spawn_department(
    self,
    spec: Dict[str, Any],
    **kwargs: Any
) -> AgentSwarm:
    """
    Spawn a department of agents like you're building a corporate hivemind fr fr.

    Args:
        spec: The department specs (more detailed than my Twitter bio)
        **kwargs: Extra config that hits different

    Returns:
        AgentSwarm: A swarm more coordinated than my life choices
    """
```

Example usage:
```python
swarm = factory.spawn_department({
    "business_unit": "growth_team",
    "budget": "infinite_money_glitch",
    "vibe": "hypergrowth"
})
```

### spawn_squad

```python
def spawn_squad(
    self,
    agents: List[AgentSpec],
    coordination: str = "hierarchical",
    **kwargs: Any
) -> AgentSquad:
    """
    Spawn a specialized squad like you're assembling an esports team.

    Args:
        agents: List of agent specs (your dream team lineup)
        coordination: How they talk to each other
        **kwargs: Extra sauce for configuration

    Returns:
        AgentSquad: A squad more synchronized than speedrunners doing co-op
    """
```

Example usage:
```python
squad = factory.spawn_squad([
    AgentSpec("researcher", skills=["data_mining", "knowledge_synthesis"]),
    AgentSpec("writer", skills=["content_generation", "meme_crafting"]),
    AgentSpec("reviewer", skills=["code_review", "vibe_check"])
])
```

## Configuration

The SwarmFactory accepts configuration that's more customizable than my VS Code setup:

```python
from smolswarms.config import SwarmConfig

config = SwarmConfig(
    base_model="claude-3-opus-20240229",  # That big brain energy
    max_tokens=8192,  # More tokens than a CS:GO inventory
    temperature=0.7,  # Spicier than my GitHub contributions
    coordination_protocol="hierarchical",  # More organized than my life
    memory_persistence="more_reliable_than_my_promises"
)
```

## Events & Callbacks

Subscribe to events like you're modding a Discord server:

```python
@factory.on("agent_spawned")
def agent_spawned_handler(agent_id: str):
    print(f"New agent just dropped: {agent_id}")

@factory.on("squad_assembled")
def squad_ready_handler(squad_id: str):
    print(f"Squad {squad_id} ready to go brr")
```

## Advanced Usage

For when you need that extra cursed energy:

```python
# Spawn a recursive swarm (it's agents all the way down)
recursive_swarm = factory.spawn_department(
    {
        "type": "recursive",
        "depth": "until_stack_overflow",
        "vibe": "more_meta_than_facebook"
    },
    allow_self_replication=True  # What could possibly go wrong?
)

# Let it evolve like it's speedrunning natural selection
recursive_swarm.evolve(
    generations="until_singularity",
    mutation_rate="yes"
)
