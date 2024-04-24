import unittest
from src.decision import Decision

class TestDecision(unittest.TestCase):
    def test_init(self):
        decision = Decision("Test Decision")
        self.assertEqual(decision.name, "Test Decision")
        self.assertEqual(decision.outcomes, [])

    def test_add_outcome(self):
        decision = Decision("Test Decision")
        outcome = "Test Outcome"
        decision.add_outcome(outcome)
        self.assertIn(outcome, decision.outcomes)

    def test_remove_outcome(self):
        decision = Decision("Test Decision")
        outcome = "Test Outcome"
        decision.add_outcome(outcome)
        decision.remove_outcome(outcome)
        self.assertNotIn(outcome, decision.outcomes)

if __name__ == '__main__':
    unittest.main()