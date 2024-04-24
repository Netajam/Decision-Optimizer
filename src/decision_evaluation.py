import numpy as np
import numpy as np

def evaluate_decision(decision, outcomes, n=1000):
    relevant_outcomes = [o for o in outcomes if o.decision == decision]
    
    all_utility_samples = []
    
    for outcome in relevant_outcomes:
        _, utility_samples = outcome.compute_utility(n)
        all_utility_samples.append(utility_samples)
    
    # Concatenate all utility samples
    final_utilities = np.concatenate(all_utility_samples)
    
    # Compute the overall expected utility
    weighted_average_utility = np.mean(final_utilities)
    
    return final_utilities, weighted_average_utility, all_utility_samples


