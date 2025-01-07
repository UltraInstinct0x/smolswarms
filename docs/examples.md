---
layout: page
title: Examples
nav_order: 4
---

# Examples 🎮

Let's see SmolSwarms in action with some examples that actually slap fr fr!

## Basic Usage 🌱

### Single Agent Example

The simplest way to get started (like your first Discord bot):

```python
from smolswarms import SwarmFactory

# Initialize the factory
factory = SwarmFactory(api_key="your-key")

# Create a basic agent
agent = factory.create_agent(
    role="researcher",
    personality="zoomer"
)

# Give it a task
result = agent.execute_task(
    "Find the latest AI papers on swarm intelligence",
    max_tokens=500
)

print(result.summary)
```

### Basic Swarm Example

When one agent isn't enough (like your Discord mod team):

```python
from smolswarms import SwarmFactory
from smolswarms.core import SwarmConfig

# Configure your swarm
config = SwarmConfig(
    swarm_size=3,
    agent_type="researcher",
    communication_style="professional"
)

# Create the swarm
factory = SwarmFactory(api_key="your-key")
swarm = factory.create_swarm(config)

# Execute a group task
results = swarm.execute_group_task(
    "Research and summarize recent developments in AI safety",
    max_tokens=1000
)

print(results.consensus_summary)
```

## Advanced Examples 🔥

### Specialized Research Swarm

Create a research team more organized than your Chrome tabs:

```python
from smolswarms import SwarmFactory
from smolswarms.agents import SpecializedAgent
from smolswarms.core import SwarmNetwork

# Create specialized agents
researcher = SpecializedAgent(
    role="lead_researcher",
    skills=["paper_analysis", "trend_spotting"]
)

analyst = SpecializedAgent(
    role="data_analyst",
    skills=["data_processing", "visualization"]
)

writer = SpecializedAgent(
    role="technical_writer",
    skills=["documentation", "communication"]
)

# Set up the network
network = SwarmNetwork()
network.add_agent(researcher, role="coordinator")
network.add_agent(analyst, role="processor")
network.add_agent(writer, role="communicator")

# Enable communication
network.enable_communication()

# Execute research pipeline
results = network.execute_pipeline([
    "gather_papers",
    "analyze_data",
    "write_report"
])
```

### Token-Optimized Swarm

Keep those API costs lower than your motivation on Monday mornings:

```python
from smolswarms import SwarmFactory
from smolswarms.utils import TokenManager, optimize_tokens

# Set up token management
manager = TokenManager(
    budget_limit=1000,
    optimization_level="aggressive"
)

# Create an optimized swarm
factory = SwarmFactory()
swarm = factory.create_swarm(
    size=5,
    token_manager=manager
)

# Monitor and optimize token usage
while swarm.is_active():
    usage = manager.get_usage()
    if usage.is_high():
        optimize_tokens(swarm, level="aggressive")

    results = swarm.execute_task(
        "Continue research with optimized tokens",
        max_tokens=100
    )
```

### Self-Improving Swarm

These agents level up faster than your gaming skills:

```python
from smolswarms import SwarmFactory
from smolswarms.core import LearningConfig

# Configure learning parameters
learning_config = LearningConfig(
    learning_rate=0.1,
    improvement_threshold=0.8,
    max_iterations=100
)

# Create a learning swarm
factory = SwarmFactory()
swarm = factory.create_learning_swarm(
    size=3,
    learning_config=learning_config
)

# Train the swarm
for epoch in range(10):
    # Execute task and learn from results
    results = swarm.execute_task_and_learn(
        "Solve complex problem with current knowledge",
        feedback_loop=True
    )

    # Check improvement
    if results.performance > 0.9:
        print("Swarm has achieved big brain energy!")
        break
```

## Error Handling Examples 🔧

Because things will break (they always do):

```python
from smolswarms import SwarmFactory
from smolswarms.exceptions import SwarmError, TokenError

# Create a factory with error handling
factory = SwarmFactory()

try:
    # Try to create a massive swarm
    swarm = factory.create_swarm(size=1000)
except SwarmError as e:
    print(f"Too many agents fr fr: {e}")
    # Fall back to a smaller swarm
    swarm = factory.create_swarm(size=10)

try:
    # Try to execute an expensive task
    results = swarm.execute_task(
        "Analyze the entire internet",
        max_tokens=1000000
    )
except TokenError as e:
    print(f"We ain't made of money: {e}")
    # Fall back to a cheaper task
    results = swarm.execute_task(
        "Analyze just Reddit instead",
        max_tokens=1000
    )
```

## Best Practices 💡

1. Start with single agents before creating swarms
2. Use specialized agents for specific tasks
3. Always implement error handling
4. Monitor and optimize token usage
5. Enable logging for debugging

## Need More Examples? 🤔

Check out our:
- [API Reference](api-reference.html) for detailed documentation
- [GitHub Repository](https://github.com/ultrainstinct0x/smolswarms/tree/main/examples) for more examples
- [Discord Community](https://discord.gg/smolswarms) for help and inspiration
