class Decision:
    def __init__(self, name):
        self.name = name
        self.outcomes = []


    def add_outcome(self, outcome):
        self.outcomes.append(outcome)

    def remove_outcome(self, outcome):
        self.outcomes.remove(outcome)

    def get_outcomes(self):
        return self.outcomes