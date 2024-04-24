import numpy as np


class Outcome:
    def __init__(self, name, decision_name, events, combine_formula, utility_function):
        self.name = name
        self.decision_name = decision_name
        self.events = events
        self.combine_formula = combine_formula
        self.utility_function = utility_function

    def generate_samples(self, n=10000):
        samples_list = [event.sample(n) for event in self.events]
        combined_samples = self.combine_formula(*samples_list)
        return combined_samples

    def compute_utility(self, n=10000):
        outcome_samples = self.generate_samples(n)
        utility_samples = self.utility_function(outcome_samples)
        expected_utility = np.mean(utility_samples)
        return expected_utility, utility_samples
