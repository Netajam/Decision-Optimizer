import unittest
from src.outcome import Outcome
from src.probabilistic_event import ProbabilisticEvent

class TestOutcome(unittest.TestCase):
    def test_init(self):
        event1 = ProbabilisticEvent("Event 1", "normal", {'mean': 0, 'std': 1})
        event2 = ProbabilisticEvent("Event 2", "uniform", {'start': 0, 'end': 1})
        outcome = Outcome("Test Outcome", "Test Decision", [event1, event2], lambda x, y: x * y, lambda x: x)
        self.assertEqual(outcome.name, "Test Outcome")
        self.assertEqual(outcome.decision_name, "Test Decision")
        self.assertEqual(len(outcome.events), 2)
        self.assertTrue(callable(outcome.combine_formula))
        self.assertTrue(callable(outcome.utility_function))

    def test_compute_utility(self):
        event = ProbabilisticEvent("Event", "normal", {'mean': 0, 'std': 1})
        outcome = Outcome("Test Outcome", "Test Decision", [event], lambda x: x, lambda x: x)
        expected_utility, utility_samples = outcome.compute_utility(n=100)
        self.assertIsInstance(expected_utility, float)
        self.assertEqual(len(utility_samples), 100)

if __name__ == '__main__':
    unittest.main()