import numpy as np
import matplotlib.pyplot as plt

def verify_probability_distribution(samples, bins=100, density=True):
    # Create a histogram
    counts, bin_edges = np.histogram(samples, bins=bins, density=density)
    # Calculate the total probability
    bin_widths = np.diff(bin_edges)
    # Similar to integrating the pdf
    total_probability = np.sum(counts * bin_widths)

    # Plotting for visual inspection
    plt.hist(samples, bins=bins, density=True)
    plt.title('Histogram of Samples')
    plt.show()

    return total_probability


