---
layout: page
title: Getting Started
nav_order: 2
---

# Getting Started with SmolSwarms 🚀

Let's get you up and running with SmolSwarms faster than you can say "recursive automation" fr fr!

## Prerequisites 📋

Before we start cooking, make sure you've got:

- Python 3.8+ installed (we ain't living in 2.7 no more)
- pip (the real ones know)
- A burning desire to spawn AI agents

## Installation 💿

```bash
# Install from PyPI (the blessed way)
pip install smolswarms

# Or if you're feeling spicy, install from source
git clone https://github.com/ultrainstinct0x/smolswarms.git
cd smolswarms
pip install -e .
```

## Your First Swarm 🐝

Let's create a simple swarm that actually does something useful (unlike my first Discord bot):

```python
from smolswarms import SwarmFactory, Agent
from smolswarms.core import SwarmConfig

# Initialize the factory with your OpenAI API key
factory = SwarmFactory(api_key="sk-...")  # Don't leak this like your Discord token

# Configure your swarm (more organized than your Chrome tabs)
config = SwarmConfig(
    swarm_size=3,  # Start small, we ain't trying to bankrupt ourselves
    agent_type="researcher",  # These agents do be researching
    communication_style="professional"  # Keep it clean in the DMs
)

# Spawn your first swarm (it's alive!)
swarm = factory.create_swarm(config)

# Give them a task (more meaningful than your average group project)
results = swarm.execute_task(
    "Research the latest developments in AI safety",
    max_tokens=1000
)

# See what they cooked up
print(results.summary)
```

## Advanced Features 🔥

### Agent Specialization

Make your agents more specialized than your Spotify playlists:

```python
from smolswarms.agents import SpecializedAgent

# Create a specialized agent (built different fr fr)
agent = SpecializedAgent(
    role="data_analyst",
    skills=["python", "pandas", "vibing"],
    personality_traits=["detail_oriented", "caffeinated"]
)

# Let it analyze some data
insights = agent.analyze_dataset("stonks.csv")
```

### Swarm Communication

Set up communication channels smoother than your Discord server:

```python
from smolswarms.core import SwarmNetwork

# Create a network (more connected than your LinkedIn)
network = SwarmNetwork()

# Add some agents to the mix
network.add_agent(agent1, role="coordinator")
network.add_agent(agent2, role="worker")

# Let them chat
network.enable_communication()
```

### Token Management

Keep those API costs lower than your motivation on Monday mornings:

```python
from smolswarms.utils import TokenManager

# Set up token management (because we ain't made of money)
manager = TokenManager(
    budget_limit=100,  # Tokens, not dollars (we responsible fr fr)
    optimization_level="aggressive"
)

# Apply it to your swarm
swarm.set_token_manager(manager)
```

## Best Practices 💡

1. **Start Small**: Don't spawn 100 agents on day one (trust the process)
2. **Monitor Token Usage**: Keep an eye on those API calls like they're your Discord notifications
3. **Use Specialized Agents**: Each agent should be more focused than a speedrunner
4. **Handle Errors Gracefully**: Because things will break (they always do)
5. **Test in Sandbox**: We ain't trying to recreate Skynet fr fr

## Common Issues 🔧

### My agents aren't communicating

```python
# Make sure you've enabled communication
swarm.enable_communication()

# Check if they're in the same network
print(swarm.network.status)
```

### Token usage is too high

```python
# Implement token optimization
from smolswarms.utils import optimize_tokens

optimize_tokens(swarm, level="aggressive")
```

### Agents are acting sus

```python
# Enable safety checks
swarm.enable_safety_protocols()

# Monitor agent behavior
swarm.set_monitoring_level("paranoid")
```

## Next Steps 🎯

Now that you're up and running:

1. Check out our [Examples](examples.html) for more inspiration
2. Read the [API Reference](api-reference.html) for the deep lore
3. Join our [Discord](https://discord.gg/smolswarms) to vibe with other developers
4. Consider [Contributing](https://github.com/ultrainstinct0x/smolswarms/blob/main/CONTRIBUTING.md) to make SmolSwarms even more based

Remember: With great power comes great responsibility... and with SmolSwarms, you've got more power than a Discord mod during a raid! 💪
