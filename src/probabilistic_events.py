from scipy.stats import norm, uniform, expon, binom, poisson

class ProbabilisticEvent:
    def __init__(self, name, distribution_type, params, complement=False):
        self.name = name
        self.distribution_type = distribution_type
        self.params = params
        self.complement = complement
        self._cached_samples = None

    def sample(self, n=10000, use_cache=True):
        if use_cache and self._cached_samples is not None:
            samples = self._cached_samples
        else:
            if self.distribution_type == 'normal':
                samples = norm.rvs(self.params['mean'], self.params['std'], size=n)
            elif self.distribution_type == 'uniform':
                samples = uniform.rvs(self.params['start'], self.params['end'] - self.params['start'], size=n)
            elif self.distribution_type == 'exponential':
                samples = expon.rvs(scale=self.params['scale'], size=n)
            elif self.distribution_type == 'binomial':
                samples = binom.rvs(self.params['n'], self.params['p'], size=n)
            elif self.distribution_type == 'poisson':
                samples = poisson.rvs(self.params['mu'], size=n)
            self._cached_samples = samples

        return 1 - samples if self.complement else samples
        
    def complementary_event(self, complement_name=None):
        if complement_name is None:
            complement_name = "N"+ self.name
        return ProbabilisticEvent(complement_name, self.distribution_type, self.params, complement=not self.complement)
