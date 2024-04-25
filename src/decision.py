class Decision:
    def __init__(self, name, outcomes=None):
        self.name = name
        self.outcomes = outcomes if outcomes is not None else []

    def add_outcome(self, outcome):
        self.outcomes.append(outcome)

    def remove_outcome(self, outcome):
        self.outcomes.remove(outcome)

    def get_outcomes(self):
        return self.outcomes