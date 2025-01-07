# SmolSwarms Core 🧠

The quantum processor of SmolSwarms fr fr - more autonomous than my coffee machine!

## What's This? 🤔

This is the core package of SmolSwarms, handling:
- Agent spawning and management (like Minecraft villagers but smarter)
- Swarm coordination (more organized than my Chrome tabs)
- Memory persistence (cleaner than my git history)

## Installation 💿

```bash
# Install from PyPI (the blessed way)
pip install smolswarms-core

# Or if you're feeling spicy, install from source
git clone https://github.com/ultrainstinct0x/smolswarms.git
cd smolswarms/packages/core
pip install -e .
```

## Quick Start 🚀

```python
from smolswarms.core import SwarmFactory, FactoryConfig, AgentRole

# Initialize the factory (more efficient than my coffee machine)
factory = SwarmFactory(
    config=FactoryConfig(
        api_key="your-key",  # Keep this secret like your Discord token
        max_agents=10,       # Don't go bankrupt
        safety_level="high"  # We ain't trying to speedrun Skynet
    )
)

# Create a single agent
agent = factory.create_agent(
    role=AgentRole.RESEARCHER,
    skills=["python", "vibing"]
)

# Or spawn a whole swarm
swarm = factory.create_swarm(
    size=3,
    roles=[AgentRole.RESEARCHER, AgentRole.ANALYST, AgentRole.COORDINATOR]
)

# Let them cook
results = await swarm.execute_group_task(
    "Research the latest developments in AI safety"
)
```

## Features 🔥

### Agent Management
- Spawn single agents or entire swarms
- Configure personalities and skills
- Monitor token usage and performance

### Swarm Coordination
- Democratic or hierarchical decision making
- Cross-agent communication
- Task distribution and result aggregation

### Memory Systems
- In-memory storage for quick access
- Persistent storage for important data
- Memory management and cleanup

## Development 🛠️

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
isort .

# Run type checks
mypy .

# Run linter
ruff check .
```

## Contributing 🤝

1. Fork it (like your favorite Discord server)
2. Create your feature branch (`git checkout -b feature/something-cool`)
3. Commit your changes (`git commit -am '✨ Add some coolness'`)
4. Push to the branch (`git push origin feature/something-cool`)
5. Create a new Pull Request

## License 📜

MIT - Because we ain't about that gatekeeping life fr fr
