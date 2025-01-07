# 🌊 smolswarms

> Because why spawn one AI when you can spawn them all? 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

smolswarms is a based framework for spawning and orchestrating autonomous AI agent swarms that actually do be hitting different fr fr. Built on top of the absolutely cracked [smolagents](https://github.com/huggingface/smolagents) library, it's like Kubernetes but for AI agents (and 100% more cursed).

## 🤔 What's the vibe?

```python
from smolswarms import SwarmFactory, AgentSpec

# Spawn your corporate hivemind in 3 lines no cap
factory = SwarmFactory()
swarm = factory.spawn_department({
    "business_unit": "growth_team",
    "budget": "infinite_money_glitch",
    "vibe": "hypergrowth"
})

# Watch the magic happen
swarm.execute_autonomously()
```

## ✨ Features that go hard

- 🏭 **Agent Factory System**: Spawn specialized AI agents faster than you can say "recursive automation"
- 🧠 **Big Brain Energy**: Uses Claude-3 as the director agent to design optimal agent architectures
- 💰 **Token Economic Policy**: Built-in optimization to keep your OpenAI bill from going to the moon
- 🤝 **Agent Communication Protocol**: They're like Discord servers but for AI agents
- 🛡️ **Safety First**: Sandboxed execution environments because we ain't trying to speedrun Skynet

## 🚀 Installation

```bash
pip install smolswarms
```

## 📚 Documentation

Check out our docs at [docs.smolswarms.ai](https://docs.smolswarms.ai) to learn:
- How to spawn your first agent swarm
- Advanced swarm orchestration patterns
- How to not accidentally create a paperclip maximizer

## 🛠️ Quick Start

```python
from smolswarms import SwarmFactory
from smolswarms.specs import BusinessUnit

# Define your swarm requirements
unit_spec = BusinessUnit(
    name="growth_team",
    core_functions=["user_acquisition", "retention", "analytics"],
    budget_constraints="reasonable"
)

# Let it cook
factory = SwarmFactory()
swarm = factory.spawn_business_unit(unit_spec)

# Run it back
results = swarm.execute_strategy("increase_q4_growth")
```

## 🤝 Contributing

PRs are welcome! Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

MIT License - go wild fam