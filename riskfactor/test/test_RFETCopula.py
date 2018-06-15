from unittest import TestCase

import numpy as np

from riskfactor.src.risk_factor_engine_t_copula import RFETCopula


class TestRFETCopula(TestCase):
    def test_volatility(self):
        spot = 100.0
        mu = 0.05
        sig = 0.2

        time_series_length = 1000.0
        time_series_sample_points = 10 ** 6
        dt = time_series_length / time_series_sample_points

        drift = (mu - 0.5 * sig * sig) * np.ones(time_series_sample_points) * dt
        diffusion = sig * np.random.normal(size=time_series_sample_points) * np.sqrt(dt)

        dlnS = drift + diffusion

        s_time_series = spot * np.exp(np.cumsum(dlnS))

        # plt.plot(np.linspace(0.0, time_series_length - dt, num=time_series_sample_points), s_time_series)
        # plt.show()

        return_time_series = s_time_series[1:] / s_time_series[:-1] - 1.0
        mu_hat = np.average(return_time_series) / dt
        sig_hat = np.std(return_time_series) / np.sqrt(dt)

        print(mu, mu_hat)
        print(sig, sig_hat)

        num_path = 10 ** 4
        rfe = RFETCopula(num_path=num_path, co_dep_data_size=time_series_sample_points, co_dep_data_shift=0,
                         decay_rate=1.0, left_percentile=0.01, right_percentile=99.99)
        ret_time_series_vol_adj = rfe.adjust_time_series_volatility(return_time_series)
        marginal_dist = rfe.generate_marginal_dist(ret_time_series_vol_adj)
        shuffle = rfe.generate_shuffle_indices(s_time_series)
        scenarios = marginal_dist[shuffle]

        mu_sim = np.average(scenarios) / dt
        sig_sim = np.std(scenarios) / np.sqrt(dt)

        print(mu, mu_sim)
        print(sig, sig_sim)

        pass

    def test_correlation(self):
        spot_1 = 100.0
        mu_1 = 0.04
        sig_1 = 0.2

        spot_2 = 200.0
        mu_2 = 0.01
        sig_2 = 0.45

        rho = 0.1

        time_series_length = 1000.0
        time_series_sample_points = 10 ** 6
        dt = time_series_length / time_series_sample_points

        norm_rand_1 = np.random.normal(size=time_series_sample_points)
        norm_rand_aux = np.random.normal(size=time_series_sample_points)
        norm_rand_2 = norm_rand_1 * rho + np.sqrt(1.0 - rho ** 2) * norm_rand_aux

        correl = np.corrcoef(norm_rand_1, norm_rand_2)
        print(correl)

        pass

    pass
