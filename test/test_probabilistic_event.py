import unittest
from src.probabilistic_event import ProbabilisticEvent

class TestProbabilisticEvent(unittest.TestCase):
    def test_init(self):
        event = ProbabilisticEvent("Test Event", "normal", {'mean': 0, 'std': 1})
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.distribution_type, "normal")
        self.assertEqual(event.params, {'mean': 0, 'std': 1})
        self.assertFalse(event.complement)

    def test_sample(self):
        event = ProbabilisticEvent("Test Event", "normal", {'mean': 0, 'std': 1})
        samples = event.sample(n=100)
        self.assertEqual(len(samples), 100)

    def test_complementary_event(self):
        event = ProbabilisticEvent("Test Event", "normal", {'mean': 0, 'std': 1})
        complement_event = event.complementary_event()
        self.assertEqual(complement_event.name, "NTest Event")
        self.assertTrue(complement_event.complement)

if __name__ == '__main__':
    unittest.main()