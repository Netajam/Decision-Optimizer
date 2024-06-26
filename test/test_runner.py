import unittest
from test_decision import TestDecision
from test_outcome import TestOutcome
from test_event import TestEvent

if __name__ == '__main__':
    test_classes = [TestDecision, TestOutcome, TestEvent]
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)