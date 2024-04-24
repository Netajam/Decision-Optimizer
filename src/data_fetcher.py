import csv
import ast
import numpy as np
from src.decision import Decision
from src.outcome import Outcome
from src.probabilistic_event import ProbabilisticEvent

def create_function_from_string(func_str):
    """
    Safely create a function from a string representation.
    Uses a restricted environment to evaluate the function, including only the 'np' module for numpy access.
    """
    try:
        # Define a restricted global environment
        safe_globals = {'np': np}
        return eval(func_str, {"__builtins__": None}, safe_globals)
    except SyntaxError as e:
        raise ValueError(f"Error creating function from string: {func_str}") from e

def load_decision_data(file_path):
    decisions = {}
    events_by_outcome = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            decision_name = row['Decision']
            if decision_name not in decisions:
                decisions[decision_name] = Decision(decision_name)

            outcome_name = row['Outcome']
            event_name = row['Event']
            event_type = row['Event_Type']
            event_params = ast.literal_eval(row['Event_Params'])
            event = ProbabilisticEvent(event_name, event_type, event_params)
            
            # Group events by outcome
            outcome_key = (decision_name, outcome_name)
            if outcome_key not in events_by_outcome:
                events_by_outcome[outcome_key] = []
            events_by_outcome[outcome_key].append(event)

    # Create outcomes with their associated events
    for (decision_name, outcome_name), events in events_by_outcome.items():
        combination_formula = create_function_from_string(row['Combination_Formula'])
        utility_function = create_function_from_string(row['Utility_Function'])
        outcome = Outcome(outcome_name, decisions[decision_name], events, combination_formula, utility_function)
        decisions[decision_name].add_outcome(outcome)

    return list(decisions.values())
