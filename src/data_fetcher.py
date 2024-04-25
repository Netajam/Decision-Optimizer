import csv
import ast
import numpy as np
from src.decision import Decision
from src.outcome import Outcome
from src.event import Event

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

def load_decision_data(events_file, outcomes_file, decisions_file):
    events = {}
    outcomes = {}
    decisions = {}

    # Load events
    with open(events_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            event_id = row['Event ID']
            event_type = row['Event Type']
            event_params = ast.literal_eval(row['Event Params'])
            utility_function = create_function_from_string(row['Utility Function'])
            events[event_id] = Event(event_id, event_type, event_params, utility_function)

    # Load outcomes
    with open(outcomes_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader: 
            outcome_id = row['Outcome ID']
            event_ids = row['Event IDs'].split(';')
            combination_formula = create_function_from_string(row['Combination Formula'])
            outcome_events = [events[event_id] for event_id in event_ids]
            outcomes[outcome_id] = Outcome(outcome_id, None, outcome_events, combination_formula)

    # Load decisions
    with open(decisions_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            decision_id = row['Decision ID']
            outcome_ids = row['Outcome IDs'].split(';')
            decision_outcomes = [outcomes[outcome_id] for outcome_id in outcome_ids]
            print(decision_outcomes)
            decisions[decision_id] = Decision(decision_id, decision_outcomes)

    return list(decisions.values())