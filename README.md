

# Decision-Optimizer based on Event Probabilities and Utility

This repository provides a Python library for making decisions based on the probability of events and their associated utility. It allows users to define probabilistic events, combine them into outcomes, and evaluate decisions based on the expected utility.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt   
    ```

## Usage

1. Import the necessary modules from the `src` package:
    ```python
    from src.probabilistic_events import ProbabilisticEvent
    from src.visualization import plot_distribution, plot_utility_distribution, plot_utility_distribution_decision, plot_probability_distribution
    from src.decisions import Decision
    from src.outcomes import Outcome
    from src.decision_evaluation import evaluate_decision
    ```

2. Define probabilistic events using the `ProbabilisticEvent` class:
    ```python
    E1 = ProbabilisticEvent("E1", "normal", {'mean': 0.3, 'std': 0.1})
    ```

3. Create decisions using the `Decision` class:
    ```python
    decision1 = Decision("Buying my train ticket")
    ```

4. Define outcomes by combining probabilistic events and specifying utility functions:
    ```python
    outcome1 = Outcome("E1&E2&E3", decision1, [E1, E2, E3], combine_formula, utility_function)
    ```

5. Evaluate decisions based on the outcomes:
    ```python
    final_utilities, weighted_average_utility, all_utility_samples = evaluate_decision(decision1, all_outcomes)
    ```

6. Visualize the probability distributions, utility distributions, and decision evaluations using the provided visualization functions.

For more detailed examples, please refer to the Jupyter notebooks in the `notebooks` directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```



