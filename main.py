import sys
sys.path.append("../src")
from src.probabilistic_event import ProbabilisticEvent
from src.visualization import plot_distribution, plot_utility_distribution, plot_utility_distribution_decision, plot_probability_distribution
from src.decision import Decision
from src.outcome import Outcome
from src.decision_evaluation import evaluate_decision
import numpy as np
import time
start_time = time.time()
# Step 1: Define and visualize individual probabilistic events
## E1: Friend1 comes
E1 = ProbabilisticEvent("E1", "normal", {'mean': 0.3, 'std': 0.1})
plot_probability_distribution(E1.sample(), "Probability of E1 occuring")
## NE1: Friend1 doesn't come
NE1= E1.complementary_event()
plot_probability_distribution(NE1.sample(), "Probability of NE1")
## Event 2: Friend 2 comes
E2 = ProbabilisticEvent("E2", "normal", {'mean': 0.6, 'std': 0.1})
plot_probability_distribution(E2.sample(), "Probability of E2 occuring")
NE2 = E2.complementary_event()
plot_probability_distribution(NE2.sample(), "Probability of event 2 not occuring")
## Event 3: Me coming
E3 = ProbabilisticEvent("E3", "uniform", {'start': 0, 'end': 1})
plot_probability_distribution(E3.sample(), "Probability of  E3 occuring")
NE3 = E3.complementary_event()
plot_probability_distribution(NE3.sample(), "Probability of event 3 not occuring")

# Step 5: Define utility function 

## Step 5.1: Utility function
def utility_function(samples):
    return 41*samples
# Step 6: Define Decisions and Outcomes
## Step 6.1: Define Decisions
decision1 = Decision("Buying my train ticket")
decision2 = Decision("Not buying my train ticket")
## Step 6.2: Define Outcomes
### Outcome 1: E1&E2&E3
outcome_title = "E1&E2&E3"
def utility_function(samples):
    return 3*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title, decision1, [E1,E2,E3], combine_formula, utility_function)
outcome1=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)


### Outcome2: E1&E3&NE3
outcome_title = "E1&E3&NE3"
def utility_function(samples):
    return 1*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title,  decision2, [E1,E2,NE3], combine_formula, utility_function)
outcome2=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)

### Outcome 3: E1&NE2&E3
outcome_title = "E1&E3&NE3"
def utility_function(samples):
    return 6*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title, decision1, [E1,NE2,E3], combine_formula, utility_function)
outcome3=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)

### Outcome 4: E1&NE2&NE3
outcome_title = "E1&NE2&NE3"
def utility_function(samples):
    return -1*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title, decision2, [E1,NE2,NE3], combine_formula, utility_function)
outcome4=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)
### Outcome 5: NE1&E2&E3
outcome_title = "NE1&E2&E3"
def utility_function(samples):
    return -2*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title, decision1, [NE1,E2,E3], combine_formula, utility_function)
outcome5=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)
### Outcome 6: NE1&E2&NE3
outcome_title = "NE1&E2&NE3"
def utility_function(samples):
    return 3*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title,  decision2, [NE1,E2,NE3], combine_formula, utility_function)
outcome6=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)
### Outcome 7: NE1&NE2&E3
outcome_title = "NE1&NE2&E3"
def utility_function(samples):
    return 4*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title, decision1, [NE1,NE2,E3], combine_formula, utility_function)
outcome7=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)
### Outcome 8: NE1&NE2&NE3
outcome_title = "NE1&NE2&NE3"
def utility_function(samples):
    return 2*samples
def combine_formula(samples1, samples2,samples3):
    return samples1* samples2*samples3


outcome = Outcome(outcome_title,  decision2, [NE1,NE2,NE3], combine_formula, utility_function)
outcome8=outcome
outcome_samples = outcome.generate_samples()
plot_distribution(outcome_samples, "Distribution of "+outcome_title)
plot_utility_distribution(outcome_samples, utility_function, 'Distribution of Utility associated t '+outcome_title)
# Step 7: Evaluate Decisions
all_outcomes = [outcome1, outcome2, outcome3, outcome4, outcome5, outcome6, outcome7, outcome8]
## Decision 1
final_utilities, weighted_average_utility, all_utility_samples = evaluate_decision(decision1, all_outcomes)
plot_utility_distribution_decision(final_utilities, weighted_average_utility, all_utility_samples, "Decision 1")
## Decision 2
final_utilities, weighted_average_utility, all_utility_samples = evaluate_decision(decision2, all_outcomes)
plot_utility_distribution_decision(final_utilities,weighted_average_utility, all_utility_samples, "Decision 2")
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Total time elapsed: {elapsed_time:.2f} seconds")