# 🌊 smolswarms

> Because why spawn one AI when you can spawn them all? 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![CI](https://github.com/UltraInstinct0x/smolswarms/actions/workflows/ci.yml/badge.svg)](https://github.com/UltraInstinct0x/smolswarms/actions/workflows/ci.yml)

smolswarms is a based framework for spawning and orchestrating autonomous AI agent swarms that actually do be hitting different fr fr. Built on top of the absolutely cracked [smolagents](https://github.com/huggingface/smolagents) library, it's like Kubernetes but for AI agents (and 100% more cursed).

## 🤔 What's the vibe?

Ever wanted to spawn an entire corporate hivemind faster than you can say "recursive automation"? smolswarms got you covered:

```python
from smolswarms import SwarmFactory, BusinessUnit

# Define your swarm requirements (more detailed than a Minecraft crafting recipe)
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

## ✨ Features that go hard

- 🏭 **Agent Factory System**: Spawns specialized AI agents faster than a Discord mod can say "no cap"
- 🧠 **Big Brain Energy**: Uses Claude-3 as the director agent to design optimal swarm architectures
- 💰 **Token Economic Policy**: Built-in optimization to keep your API costs from going to the moon
- 🤝 **Agent Communication Protocol**: They're like Discord servers but for AI agents fr fr
- 🛡️ **Safety First**: Sandboxed execution environments because we ain't speedrunning the robot apocalypse

## 🚀 Quick Installation

```bash
# Install with pip (straight from the source no cap)
pip install git+https://github.com/UltraInstinct0x/smolswarms.git
```

## 📚 Advanced Installation

For development mode with all the debug tools (like you're trying to find glitches in the matrix):

```bash
git clone https://github.com/UltraInstinct0x/smolswarms.git
cd smolswarms
pip install -e .[dev]  # Install that developer%
```

## 🛠️ Usage

Here's how to spawn your first agent swarm (it's like playing God but with Python):

```python
from smolswarms import SwarmFactory
from smolswarms.specs import AgentSpec

# Create a factory that's more optimized than a TAS speedrun
factory = SwarmFactory()

# Define your agent specs (like character creation but for AI)
specs = [
    AgentSpec(role="researcher", skills=["data_analysis", "paper_reading"]),
    AgentSpec(role="writer", skills=["content_generation", "meme_crafting"]),
    AgentSpec(role="reviewer", skills=["code_review", "vibe_check"])
]

# Spawn the whole squad
swarm = factory.spawn_swarm(specs)

# Let them cook
swarm.execute_task("make_this_repo_more_based")
```

## 🤝 Contributing

PRs are welcome! Just follow these steps that are more organized than a speedrunner's hotkey setup:

1. Fork it (`https://github.com/UltraInstinct0x/smolswarms/fork`)
2. Create your feature branch (`git checkout -b feature/something_fire`)
3. Make your changes (more heat than a Discord server during drama)
4. Run the tests (`pytest` - because we ain't pushing bugs to prod fr fr)
5. Commit your changes (`git commit -am 'feat: added something absolutely cracked'`)
6. Push to the branch (`git push origin feature/something_fire`)
7. Create a new Pull Request

### Development Requirements

- Python 3.10+ (we using that future syntax fr fr)
- Development dependencies (`pip install -e .[dev]`)
- A sense of humor (required for reading the codebase)

## 🔬 Testing

Run tests like you're trying to speedrun a 100% completion:

```bash
# Run all tests
pytest

# Run with coverage (see what parts of the code never got executed)
pytest --cov=smolswarms

# Run specific test file (when you know exactly what you broke)
pytest tests/test_specific_feature.py
```

## 📝 License

MIT License - go wild fam (but responsibly) 🚀

## 🤖 Integration with OpenHands

Need help fixing bugs or implementing features? Just tag `@openhands-agent` in your issue or PR:

```markdown
Hey @openhands-agent, this feature be acting more cursed than a Python script with mixed tabs and spaces. Help a dev out?
```

The agent will analyze your issue and try to fix it faster than a speedrunner finding a new glitch! 

## ⚠️ Safety Notice

While smolswarms is designed to be more autonomous than a Tesla on autopilot, remember:
- Don't give agents access to prod without supervision
- Keep API costs under control (no infinite token glitch)
- Monitor agent behavior (they do be learning fr fr)

Need help or got questions? Drop an issue or hit us up - we're more responsive than a Discord mod during a raid! 🎮