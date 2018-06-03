import numpy as np


class Utils(object):
    @staticmethod
    def percentile(source_array: list, percentiles: list):
        vec = np.array(source_array)
        vec.sort()
        pct = np.array(percentiles) / 100.0
        if np.any(pct > 1.0) or np.any(pct < 0.0):
            raise ValueError('percentile should between 0 and 100, inclusive.')

        shift = 0.5 / vec.size
        interp_pos = (pct - shift).__mul__(vec.size)
        interp_idx = interp_pos.astype(int)
        interp_idx = np.maximum(np.minimum(interp_idx, vec.size - 2), 0)
        interp_weight = interp_pos - interp_idx
        projected_array = vec[interp_idx] + interp_weight * (vec[interp_idx + 1] - vec[interp_idx])
        projected_array[pct < shift] = vec[0]  # left tail extrapolation
        projected_array[pct > (1.0 - shift)] = vec[-1]  # right tail extrapolation
        return projected_array

    pass


class CSRandom(object):
    __BIG_INT = 2147483647
    __BIG_SEED = 161803398
    __RANGE = 55
    __BREAK = 21

    def __init__(self, seed: int):
        self.seed = seed
        self.__seed_array = self.__gen_seed_array()
        self.__index = 0

    def __gen_seed_array(self):
        seed_array = np.zeros(self.__RANGE, dtype=int)
        seed_array[0], seed_array[1] = self.__BIG_SEED - self.seed, 1
        for idx in range(2, self.__RANGE):
            seed_array[idx] = self.__bound_int(seed_array[idx - 2] - seed_array[idx - 1])
        seed_array = seed_array[::-1]
        shuffle_order = np.array([(self.__BREAK * x) % self.__RANGE - 1 for x in range(self.__RANGE)], dtype=int)[::-1]
        seed_array = seed_array[shuffle_order]
        shuffle_order = [(x + 31) % self.__RANGE for x in range(self.__RANGE)]
        for _ in range(4):
            for idx in range(self.__RANGE):
                seed_array[idx] = self.__bound_int(seed_array[idx] - seed_array[shuffle_order[idx]])
        return seed_array

    def next_uniform(self, n: int = 1):
        pos_vec = np.zeros(n, dtype=float)
        for idx in range(n):
            self.__index %= self.__RANGE
            index_rear = (self.__index + self.__BREAK) % self.__RANGE
            pos = self.__bound_int(self.__seed_array[self.__index] - self.__seed_array[index_rear])
            self.__seed_array[self.__index] = pos
            pos_vec[idx] = pos
            self.__index += 1
        return pos_vec / self.__BIG_INT

    def __bound_int(self, value: int):
        return value if value > 0 else value + self.__BIG_INT

    pass


class GeneralizedParetoDistribution(object):
    def __init__(self, xi: float, mu: float = 0.0, sig: float = 1.0):
        self._xi = xi
        self._mu = mu
        self._sig = sig
        if self._xi < 0.0:
            raise AttributeError('expect non-negative xi')
        if self._sig <= 0.0:
            raise AttributeError('expect volatility greater than zero')
        pass

    def cdf(self, x_array: np.ndarray):
        u_array = np.maximum((x_array - self._mu) / self._sig, 0.0)
        if abs(self._xi) < 1e-12:
            u_array = 1.0 - np.exp(-u_array)
        else:
            u_array = 1.0 - np.power(1.0 + self._xi * u_array, -1.0 / self._xi)
        return u_array

    def ppf(self, u_array: np.ndarray):
        if np.any(u_array < 0.0) or np.any(u_array >= 1.0):
            raise AttributeError('inverse array must be in [0.0, 1.0)')
        if abs(self._xi) < 1e-12:
            x_array = -np.log(1.0 - np.array(u_array, dtype=float))
        else:
            x_array = (np.power(1.0 - np.array(u_array, dtype=float), -self._xi) - 1.0) / self._xi
        return x_array * self._sig + self._mu

    @staticmethod
    def fit_given_mu(x_array: np.array, u_array: np.array = None, mu: float = 0.0, sig_guess: float = 1.0,
                     xi_guess: float = 1e-10):

        model = GeneralizedParetoDistribution(xi=xi_guess, mu=mu, sig=sig_guess)
        err = model.__calculate_cost()

        return model

    def __calculate_cost(self):
        return 0.0

    pass
