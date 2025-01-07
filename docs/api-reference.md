---
layout: page
title: API Reference
nav_order: 3
---

# API Reference 📚

Welcome to the sacred texts fr fr. Here's everything you need to know about SmolSwarms' API.

## Core Components 🧱

### SwarmFactory

The blessed way to spawn your agents:

```python
from smolswarms import SwarmFactory

factory = SwarmFactory(
    api_key="your-key",  # Keep this secret like your Discord token
    max_agents=10,       # Don't go bankrupt
    safety_level="high"  # We ain't trying to speedrun Skynet
)
```

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `create_agent()` | Spawns a single agent | `Agent` |
| `create_swarm()` | Spawns multiple agents | `Swarm` |
| `get_agent_count()` | How many agents you've spawned | `int` |

### Agent

The building block of your swarm:

```python
from smolswarms import Agent

agent = Agent(
    role="researcher",
    personality="zoomer",
    skills=["python", "vibing"]
)
```

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `execute_task()` | Makes the agent do something | `TaskResult` |
| `communicate()` | Slides into other agents' DMs | `Message` |
| `learn()` | Levels up the agent's skills | `None` |

### Swarm

A collection of agents working together:

```python
from smolswarms import Swarm

swarm = Swarm(
    agents=[agent1, agent2],
    coordination_style="democratic"
)
```

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `execute_group_task()` | Coordinated action | `GroupResult` |
| `add_agent()` | Expands the squad | `None` |
| `remove_agent()` | Kicks an agent | `None` |

## Utilities 🛠️

### TokenManager

Keeps your API costs lower than your motivation on Monday mornings:

```python
from smolswarms.utils import TokenManager

manager = TokenManager(
    budget_limit=1000,
    optimization_level="aggressive"
)
```

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `get_usage()` | Check your spending | `TokenUsage` |
| `optimize()` | Save some tokens | `None` |
| `set_limit()` | Budget control | `None` |

### SwarmNetwork

Sets up communication channels smoother than your Discord server:

```python
from smolswarms.core import SwarmNetwork

network = SwarmNetwork(
    topology="mesh",
    encryption="enabled"
)
```

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `connect()` | Links agents | `None` |
| `broadcast()` | Send to all agents | `None` |
| `get_status()` | Network health check | `Status` |

## Error Handling 🔧

Because things will break (they always do):

```python
from smolswarms.exceptions import (
    SwarmError,
    AgentError,
    TokenError
)

try:
    result = agent.do_something_risky()
except SwarmError as e:
    print(f"Swarm's not feeling it: {e}")
except AgentError as e:
    print(f"Agent's having a moment: {e}")
except TokenError as e:
    print(f"We broke fr fr: {e}")
```

## Configuration 🎮

Example configuration object:

```python
from smolswarms.core import SwarmConfig

config = SwarmConfig(
    swarm_size=5,
    agent_type="researcher",
    communication_style="professional",
    token_limit=1000,
    safety_checks=True,
    logging_level="debug"
)
```

## Best Practices 💡

1. Always use `SwarmFactory` to create agents
2. Handle errors more gracefully than a cat landing on its feet
3. Monitor token usage like your Discord notifications
4. Use type hints (we ain't trying to play type guessing games)
5. Test in sandbox mode first (trust the process)

## Need Help? 🆘

- Check the [Examples](examples.html) for inspiration
- Join our [Discord](https://discord.gg/smolswarms)
- Report bugs on [GitHub](https://github.com/ultrainstinct0x/smolswarms/issues)
- Read the [Contributing Guide](https://github.com/ultrainstinct0x/smolswarms/blob/main/CONTRIBUTING.md)
