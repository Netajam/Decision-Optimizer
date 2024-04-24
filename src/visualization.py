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




def plot_utility_distribution_decision(final_utilities, weighted_average_utility, all_utility_samples, title):
    plt.figure()
    

    # Plot utility distribution for each outcome
    for idx, utility_samples in enumerate(all_utility_samples):
      
        sns.kdeplot(utility_samples, label=f'Outcome KDE {idx + 1}')
    
    plt.hist(final_utilities, bins=50, density=True, alpha=0.5, label=f'Decision Utility')
    
    plt.title(f'Utility Distributions for {title}', color='white')
    plt.xlabel('Utility', color='white')
    plt.ylabel('Density', color='white')
    plt.tick_params(colors='white')
    plt.legend()
    plt.show()
    print_statistics(final_utilities, f'Decision Utility for {title}')
