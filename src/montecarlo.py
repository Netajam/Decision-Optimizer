def monte_carlo(event1, event2, combine_formula, n=10000):
    samples1 = event1.sample(n)
    samples2 = event2.sample(n)
    combined_samples = combine_formula(samples1, samples2)
    return combined_samples
