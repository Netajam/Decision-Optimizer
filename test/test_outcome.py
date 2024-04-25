import unittest
import numpy as np
from src.outcome import Outcome
from src.event import Event

# Mock implementation for Event class to make the example self-contained
class Event:
    def __init__(self, name, distribution_type, parameters):
        self.name = name
        self.distribution_type = distribution_type
        self.parameters = parameters
        # Mock sample and utility arrays
        if distribution_type == "normal":
            self.samples = np.random.normal(parameters['mean'], parameters['std'], 100)
            self.utilities = self.samples ** 2  # Example utility calculation
        elif distribution_type == "uniform":
            self.samples = np.random.uniform(parameters['start'], parameters['end'], 100)
            self.utilities = self.samples  # Example utility calculation

class TestOutcome(unittest.TestCase):
    def test_init(self):
        event1 = Event("Event 1", "normal", {'mean': 0, 'std': 1})
        event2 = Event("Event 2", "uniform", {'start': 0, 'end': 1})
        outcome = Outcome("Test Outcome", "Test Decision", [event1, event2], np.multiply)
        self.assertEqual(outcome.name, "Test Outcome")
        self.assertEqual(outcome.decision_name, "Test Decision")
        self.assertEqual(len(outcome.events), 2)
        self.assertTrue(callable(outcome.combine_formula))
        self.assertIsNotNone(outcome.samples)
        self.assertIsNotNone(outcome.expected_utility)

    def test_compute_utility(self):
        event1 = Event("Event 1", "normal", {'mean': 0, 'std': 1})
        outcome = Outcome("Test Outcome", "Test Decision", [event1], np.square)
        self.assertIsInstance(outcome.expected_utility, float)
        self.assertEqual(len(outcome.utilities), 100)
        self.assertAlmostEqual(outcome.expected_utility, np.mean(outcome.utilities), places=5)

if __name__ == '__main__':
    unittest.main()
