import numpy as np


class CSRandom(object):
    __BIG = 2147483647
    __DRIFT = 161803398
    __RANGE = 55
    __GAP = 21

    def __init__(self, seed: int):
        self.seed = seed
        self.__seed_array = self.__gen_seed_array()
        self.__index = 0

    def __gen_seed_array(self):
        arr = np.zeros(self.__RANGE, dtype=int)
        arr[0], arr[1] = self.__DRIFT - self.seed, 1
        for idx in range(2, self.__RANGE):
            arr[idx] = self.__bound_int(arr[idx - 2] - arr[idx - 1])
        arr = arr[::-1]
        shuffle_order = np.array([(self.__GAP * x) % self.__RANGE - 1 for x in range(self.__RANGE - 1, -1, -1)], dtype=int)
        arr = arr[shuffle_order]
        shuffle_order = [(x + 31) % self.__RANGE for x in range(self.__RANGE)]
        for _ in range(4):
            for idx in range(self.__RANGE):
                arr[idx] = self.__bound_int(arr[idx] - arr[shuffle_order[idx]])
        return arr

    def next_uniform(self, n: int = 1):
        pos_vec = np.zeros(n, dtype=float)
        for idx in range(n):
            self.__index %= self.__RANGE
            index_rear = (self.__index + self.__GAP) % self.__RANGE
            pos = self.__bound_int(self.__seed_array[self.__index] - self.__seed_array[index_rear])
            self.__seed_array[self.__index] = pos
            pos_vec[idx] = pos
            self.__index += 1
        return pos_vec / self.__BIG

    def __bound_int(self, value: int):
        return value if value > 0 else value + self.__BIG
