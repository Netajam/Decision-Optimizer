import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import cumfreq
import seaborn as sns

def print_statistics(samples, label):
    print(f"Statistics for {label}:")
    print(f"  Mean: {np.mean(samples):.2f}")
    print(f"  Median: {np.median(samples):.2f}")
    print(f"  Standard Deviation: {np.std(samples):.2f}")
    print(f"  25th percentile: {np.percentile(samples, 25):.2f}")
    print(f"  75th percentile: {np.percentile(samples, 75):.2f}")

def plot_distribution(samples, title):
    plt.figure()
    
    # Plot PDF
    plt.hist(samples, bins=50, density=True, alpha=0.5, label='PDF')
    
    # Plot CDF
    a, edges = np.histogram(samples, bins=50, density=True)
    cum_a = np.cumsum(a)
    plt.plot(edges[1:], cum_a/np.max(cum_a), label='CDF')
    
    plt.title(title, color='white')
    plt.xlabel('Value', color='white')
    plt.ylabel('Frequency', color='white')
    
    # Changing tick colors to white
    plt.tick_params(colors='white')

    plt.grid(True)
    plt.legend()
 
    plt.show()
    print_statistics(samples, title)

def plot_probability_distribution(samples, title):
    fig, ax1 = plt.subplots()

    # Plot PDF on the first set of axes (ax1)
    ax1.hist(samples, bins=50, density=True, alpha=0.5, label='PDF')
    ax1.set_xlabel('Value', color='white')
    ax1.set_ylabel('Density', color='white')
    ax1.tick_params(axis='y', colors='white')
    ax1.tick_params(axis='x', colors='white')

    # Create a second set of axes sharing the x-axis with ax1
    ax2 = ax1.twinx()

    # Plot CDF on the second set of axes (ax2)
    a, edges = np.histogram(samples, bins=50, density=True)
    cum_a = np.cumsum(a)
    ax2.plot(edges[1:], cum_a / np.max(cum_a), 'g-', label='CDF')
    ax2.set_ylabel('CDF', color='green')
    ax2.tick_params(axis='y', colors='green')

    ax1.set_title(title, color='white')
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.grid(True)
    plt.show()

    


def plot_utility_distribution(samples, utility_function, title):
    utility_samples = utility_function(samples)
    plt.figure()
    plt.hist(utility_samples, bins=50, density=True, alpha=0.5, label=f'Utility of {title}')
    
    # Plot Mean
    mean_val = np.mean(utility_samples)
    plt.axvline(mean_val, color='r', linestyle='--')
    plt.text(mean_val, 0, f'Mean: {mean_val:.2f}', rotation=0, color='red')
    
    # Plot Median
    median_val = np.median(utility_samples)
    plt.axvline(median_val, color='g', linestyle='--')
    plt.text(median_val, 0, f'Median: {median_val:.2f}', rotation=0, color='green')

    # Plot Standard Deviation
    std_dev = np.std(utility_samples)
    plt.axvline(mean_val - std_dev, color='b', linestyle='--')
    plt.axvline(mean_val + std_dev, color='b', linestyle='--')
    plt.text(mean_val + std_dev, 0, f'Std Dev: {std_dev:.2f}', rotation=0, color='blue')

    # Plot Quartiles (25th and 75th percentile)
    q25, q75 = np.percentile(utility_samples, [25, 75])
    plt.axvline(q25, color='y', linestyle='--')
    plt.axvline(q75, color='y', linestyle='--')
    plt.text(q25, 0, f'25th: {q25:.2f}', rotation=0, color='yellow')
    plt.text(q75, 0, f'75th: {q75:.2f}', rotation=0, color='yellow')
    
    plt.title('Utility Distributions', color='white')
    plt.xlabel('Utility', color='white')
    plt.ylabel('Density', color='white')
    plt.tick_params(colors='white')
    plt.legend()
    plt.show()
    print_statistics(utility_samples, f'Utility of {title}')




def plot_decision_utility_distribution(decision, utility_samples_list, title, colors=None, fig_size=(10, 6)):
    """
    Plot the utility distribution for each outcome of a decision and the overall decision utility.

    Args:
        decision (Decision): The decision object containing the outcomes.
        utility_samples_list (list): A list of utility sample arrays for each outcome.
        title (str): The title of the plot.
        colors (list, optional): A list of colors for each outcome. If not provided, default colors will be used.
        fig_size (tuple, optional): The size of the figure in inches (width, height). Default is (10, 6).

    Returns:
        None
    """
    plt.figure(figsize=fig_size)
    if colors is None:
        colors = ['C{}'.format(i) for i in range(len(utility_samples_list))]

    for i, (outcome, utility_samples, color) in enumerate(zip(decision.get_outcomes(), utility_samples_list, colors)):
        sns.kdeplot(utility_samples, label=f'{outcome.name}', color=color, linewidth=2, alpha=0.7, linestyle='--')

        plt.axvline(np.mean(utility_samples), color=color, linestyle='--', linewidth=1.5,
                    label=f'{outcome.name} (Mean)')

    overall_utility_samples = np.concatenate(utility_samples_list)

    # Plot the overall decision utility as a curve with a plain line
    sns.kdeplot(overall_utility_samples, label='Overall Decision Utility', color='black', linewidth=3, alpha=0.7)

    # Plot the overall decision utility as a bar chart
    plt.hist(overall_utility_samples, bins=50, density=True, alpha=0.5, label='_nolegend_')

    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Utility', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.tick_params(labelsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.25, 1))

    x_min, x_max = np.min(overall_utility_samples), np.max(overall_utility_samples)
    x_range = x_max - x_min
    plt.xlim(x_min - 0.1 * x_range, x_max + 0.1 * x_range)

    y_max = plt.ylim()[1]
    plt.ylim(0, y_max * 1.1)

    plt.tight_layout()
    plt.show()

    print_statistics(overall_utility_samples, 'Overall Decision Utility')