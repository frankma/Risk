import numpy as np


class Utils(object):
    @staticmethod
    def percentile(source_array: np.ndarray, percentiles: list):
        vec = np.array(source_array, dtype=float)
        vec.sort()
        pct = np.array(percentiles, dtype=float) / 100.00
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


class GenParetoDist(object):
    def __init__(self, xi: float, location: float = 0.0, scale: float = 1.0, direction: float = 1.0):
        self._xi = xi
        self._location = location
        self._scale = scale
        self._direction = direction
        if self._scale <= 0.0:
            raise AttributeError('expect volatility greater than zero')
        if abs(abs(direction) - 1) > 1e-12:
            raise AttributeError('direction must be either 1 or -1')
        pass

    def cdf(self, x_arr: np.ndarray):
        u_arr = np.maximum((x_arr - self._location) / self._scale, 0.0) * self._direction
        if abs(self._xi) < 1e-12:
            u_arr = 1.0 - np.exp(-u_arr)
        else:
            u_arr = 1.0 - np.power(1.0 + self._xi * u_arr, -1.0 / self._xi)
        return u_arr

    def ppf(self, u_arr: np.ndarray):
        if np.any(u_arr < 0.0) or np.any(u_arr >= 1.0):
            raise AttributeError('inverse array must be in [0.0, 1.0)')
        if abs(self._xi) < 1e-12:
            x_arr = -np.log(1.0 - np.array(u_arr, dtype=float))
        else:
            x_arr = (np.power(1.0 - np.array(u_arr, dtype=float), -self._xi) - 1.0) / self._xi
        x_arr = x_arr if self._direction > 0.0 else x_arr[::-1]
        return x_arr * self._scale * self._direction + self._location

    @staticmethod
    def fit_given_loc(x_arr: np.array, loc: float = 0.0, scale_guess: float = 1.0, xi_guess: float = 1e-10,
                      iter_max: int = 500, cost_threshold: float = 1e-12, step_threshold: float = 1e-10,
                      shock: float = 1e-5):
        x_arr_loc_adj = np.array(x_arr - loc, dtype=float)
        if np.all(x_arr_loc_adj < 0.0):
            direction = -1
        elif np.all(x_arr_loc_adj > 0.0):
            direction = 1
        else:
            raise ValueError('expect data array to be singled sided to loc')
        x_arr_loc_adj *= direction
        x_arr_loc_adj.sort()

        cost = 100.0
        step_relative = scale_guess / 10.0
        step_absolute = 0.01
        scale = scale_guess
        scale_step = -10.0
        xi = xi_guess
        xi_step = 10.0
        iter_count = 0

        nll = GenParetoDist.__calc_nll(x_arr_loc_adj, scale, xi)

        while cost > cost_threshold and max(abs(xi_step), abs(scale_step)) > step_threshold and iter_count < iter_max:
            scale_slope = (GenParetoDist.__calc_nll(x_arr_loc_adj, scale + shock, xi) - nll) / shock
            xi_slope = (GenParetoDist.__calc_nll(x_arr_loc_adj, scale, xi + shock) - nll) / shock
            slope_norm = max(abs(scale_slope), abs(xi_slope))

            step_length = step_absolute if abs(xi_slope) == abs(slope_norm) else step_relative
            scale_step = scale_slope / slope_norm * step_length
            xi_step = xi_slope / slope_norm * step_length

            scale_descent = scale - scale_step if scale > abs(scale_step) else scale
            xi_descent = min(xi - xi_step if abs(xi - xi_step) > 1e-10 else 1e-10, 1.0)
            nll_descent = GenParetoDist.__calc_nll(x_arr_loc_adj, scale_descent, xi_descent)

            if nll_descent > nll:
                step_relative /= 2.0
                step_absolute /= 2.0
            else:
                scale = scale_descent
                xi = xi_descent
                cost = abs(nll - nll_descent)
                nll = nll_descent

            iter_count += 1

        return GenParetoDist(xi=xi, location=loc, scale=scale, direction=direction)

    @staticmethod
    def __calc_nll(x_arr_loc_adj: np.array, scale: float, xi: float):
        err_vec = np.log(1.0 + xi * x_arr_loc_adj / scale)
        nll = np.sum(err_vec) * (1.0 + 1.0 / xi) if (abs(xi) > 1e-12) else np.sum(err_vec)
        nll += np.log(scale) * err_vec.size
        if xi < 0.0:
            nll += 10.0 * max(max(err_vec) + scale / xi, 0.0)
        return nll

    pass
