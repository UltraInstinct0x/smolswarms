---
layout: default
title: Quick Start Guide
parent: Guides
nav_order: 1
---

# Quick Start Guide
{: .no_toc }

Getting started with SmolSwarms faster than a speedrunner finding a new glitch fr fr 🏃‍♂️
{: .fs-6 .fw-300 }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Installation

First, let's get this bad boy installed faster than npm downloading node_modules:

```bash
pip install smolswarms
```

Want that developer% speedrun strats?

```bash
git clone https://github.com/ultrainstinct0x/smolswarms.git
cd smolswarms
pip install -e .[dev]  # Install that developer DLC
```

## Basic Usage

Creating your first swarm is easier than explaining why you have 47 Chrome tabs open:

```python
from smolswarms import SwarmFactory
from smolswarms.specs import BusinessUnit

# Define your swarm requirements (more detailed than my coffee order)
unit_spec = BusinessUnit(
    name="growth_team",
    core_functions=["user_acquisition", "retention", "analytics"],
    budget_constraints="reasonable"  # No infinite money glitch... yet
)

# Let it cook fr fr
factory = SwarmFactory()
swarm = factory.spawn_business_unit(unit_spec)

# Watch the magic happen
results = swarm.execute_strategy("increase_q4_growth")
print(f"Swarm do be vibing: {results}")
```

## Configuration

Configure your swarm like you're optimizing your Discord server settings:

```python
from smolswarms.config import SwarmConfig

config = SwarmConfig(
    base_model="claude-3-opus-20240229",  # That big brain energy
    max_tokens=8192,  # More tokens than a CS:GO inventory
    temperature=0.7,  # Spicier than my GitHub contributions
    coordination_protocol="hierarchical"  # More organized than my life
)

# Apply config like it's a texture pack
factory = SwarmFactory(config=config)
```

## Advanced Features

### Agent Communication

Make your agents talk to each other like they're in a Discord server:

```python
# Create a communication channel that hits different
channel = swarm.create_channel("strategy_discussion")

# Let them chat fr fr
swarm.broadcast(
    channel=channel,
    message="Yo, who's trying to optimize this workflow rn?",
    priority="high"
)
```

### Memory Management

Give your agents memory persistence that's more reliable than my promises to fix legacy code:

```python
# Save that knowledge like it's a game checkpoint
swarm.store_memory(
    key="market_insights",
    value={"trend": "up only", "confidence": "trust_me_bro"},
    persistence="permanent"
)

# Retrieve it faster than my excuse generator
insights = swarm.recall_memory("market_insights")
```

## What's Next?

- Check out our [Advanced Guides](advanced.md) for more galaxy brain strats
- Join our [Discord](https://discord.gg/smolswarms) to vibe with the dev team
- Read the [Architecture Guide](architecture.md) to understand how this quantum realm works
- Browse the [API Reference](/reference) for that low-level knowledge

Remember: With great power comes great API costs - use responsibly fr fr! 💫
