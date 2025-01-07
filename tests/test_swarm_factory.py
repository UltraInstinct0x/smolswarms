import unittest
from smolswarms.swarm_factory import SwarmFactory

class TestSwarmFactory(unittest.TestCase):
    def test_spawn_department_optimize_tokens(self):
        factory = SwarmFactory()
        swarm = factory.spawn_department({
            "business_unit": "test_team",
            "budget": "optimize_tokens",
            "vibe": "test_vibe"
        })
        self.assertIsNone(swarm)  # Add more specific assertions based on expected behavior

    def test_spawn_department_default_budget(self):
        factory = SwarmFactory()
        swarm = factory.spawn_department({
            "business_unit": "test_team",
            "budget": "default",
            "vibe": "test_vibe"
        })
        self.assertIsNone(swarm)  # Add more specific assertions based on expected behavior

if __name__ == '__main__':
    unittest.main()
