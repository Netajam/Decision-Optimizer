import csv
from .probabilistic_event import ProbabilisticEvent
from .decision import Decision
from .outcome import Outcome

def load_decision_data(file_path, n_samples=10000):
    decisions = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            decision_name = row['Decision']
            outcome_name = row['Outcome']
            event_name = row['Event']
            event_type = row['Event_Type']
            event_params = eval(row['Event_Params'])
            utility_function = eval(row['Utility_Function'])
            combination_formula_str = row['Combination_Formula']
            
            if decision_name not in decisions:
                decisions[decision_name] = Decision(decision_name)
            
            event = ProbabilisticEvent(event_name, event_type, event_params)
            
            # Generate samples for the event
            event_samples = event.sample(n_samples)
            
            # Create the lambda function dynamically
            combination_formula = eval(f"lambda samples: {combination_formula_str}")
            
            # Combine the event samples using the combination formula
            combined_samples = combination_formula(event_samples)
            
            outcome = Outcome(outcome_name, decisions[decision_name], [event], combined_samples, utility_function)
            decisions[decision_name].add_outcome(outcome)
    
    return list(decisions.values())

