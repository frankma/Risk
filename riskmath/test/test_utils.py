from unittest import TestCase

import numpy as np
from scipy.stats import genpareto

from riskmath.src.utils import GenParetoDist


class TestUtils(TestCase):
    def test_percentile(self):
        pass

    pass


class TestCSRandom(TestCase):
    def test_next_uniform(self):
        pass

    pass


class TestGeneralizedParetoDistribution(TestCase):
    def test_cdf(self):
        xi = 0.1
        mu = 0.05
        sig = 0.5

        model = GenParetoDist(xi, mu, sig)
        model_sp = genpareto(c=xi, loc=mu, scale=sig)

        xs = np.array(np.linspace(0.0, 10.0), dtype=float)

        vec = model.cdf(xs)
        vec_sp = model_sp.cdf(xs)

        for idx in range(xs.__len__()):
            self.assertAlmostEqual(vec[idx], vec_sp[idx], delta=1e-10)

        pass

    def test_ppf(self):
        xi = 0.1
        mu = 0.05
        sig = 0.5

        model = GenParetoDist(xi, mu, sig)
        model_sp = genpareto(c=xi, loc=mu, scale=sig)

        us = np.array(np.linspace(0.01, 0.99), dtype=float)

        vec = model.ppf(us)
        vec_sp = model_sp.ppf(us)

        for idx in range(us.__len__()):
            self.assertAlmostEqual(vec[idx], vec_sp[idx], delta=1e-10)

        pass

    def test_fit_given_loc(self):

        pass

    pass
