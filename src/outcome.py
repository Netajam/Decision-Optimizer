import numpy as np
from src.event import Event
class Outcome:
    def __init__(self, name, decision_name, events:Event, combine_formula, utility_formula=None):
        self.name = name
        self.decision_name = decision_name
        self.events = events
        self.combine_formula = combine_formula
        self.utility_formula = utility_formula
        self.samples=self.generate_samples()
        self.expected_utility, self.utilities = self.compute_utility()

    def generate_samples(self):
        # With resampling
        # samples_list = [event.sample(n) for event in self.events]
        # without resampling
        samples_list = [event.samples for event in self.events]
        combined_samples = self.combine_formula(*samples_list)
        return combined_samples

    def compute_utility(self):
        ## Without resampling
        utility_samples = [event.utilities for event in self.events]
        combined_utility = self.combine_formula(*utility_samples) if self.utility_formula is None else self.utility_formula(self.samples)
        expected_utility = np.mean(combined_utility)
        return expected_utility, combined_utility