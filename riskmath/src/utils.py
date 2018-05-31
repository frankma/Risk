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
