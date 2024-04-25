from scipy.stats import norm, uniform, expon, binom, poisson

class Event:
    def __init__(self, name, distribution_type, params, utility_function=None, complement=False,n=1000):
        self.name = name
        self.distribution_type = distribution_type
        self.params = params
        self.utility_function = utility_function if utility_function is not None else lambda x:x
        self.complement = complement 
        self.samples = self.sample()
        self.utilities = self.compute_utility(self.samples)
        self.n=n

    def sample(self, n=10000):
        if self.distribution_type == 'normal':
            samples = norm.rvs(self.params['mean'], self.params['std'], size=n)
        elif self.distribution_type == 'uniform':
            samples = uniform.rvs(self.params['start'], self.params['end'] - self.params['start'], size=n)
        elif self.distribution_type == 'exponential':
            samples = expon.rvs(scale=self.params['scale'], size=n)
        elif self.distribution_type == 'binomial':
            samples = binom.rvs(1, self.params['p'], size=n)
        elif self.distribution_type == 'poisson':
            samples = poisson.rvs(self.params['mu'], size=n)
        return 1 - samples if self.complement else samples

    def complementary_event(self, complement_name=None):
        complement_params = self.params.copy()
        if self.distribution_type == 'binomial':
            complement_params['p'] = 1 - complement_params['p']
        elif self.distribution_type == 'poisson':
            complement_params['mu'] = -complement_params['mu']
        if complement_name is None:
            complement_name = "Not " + self.name
        return Event(complement_name, self.distribution_type, complement_params, lambda x: -self.utility_function(1 - x), complement=not self.complement)

    def compute_utility(self, samples):
        return self.utility_function(samples)