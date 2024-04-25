import numpy as np
import numpy as np

def evaluate_decision(outcomes, n=1000):
    all_utility_samples = []
    for outcome in outcomes:
        _, utility_samples = outcome.compute_utility()
        all_utility_samples.append(utility_samples)

    final_utilities = np.concatenate(all_utility_samples)
    weighted_average_utility = np.mean(final_utilities)
    return final_utilities, weighted_average_utility, all_utility_samples
