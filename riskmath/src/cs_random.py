import numpy as np


class CSRandom(object):
    BIG_INT = 2147483647
    Z = 0
    M_SEED = 161803398

    def __init__(self, seed: int):
        self.seed = seed
        self.seed_array = self.__gen_seed_array()

    def __gen_seed_array(self):
        arr = np.zeros(55, dtype=int)
        arr[0], arr[1] = self.M_SEED - self.seed, 1
        for idx in range(2, 55):
            arr[idx] = self.__bound_int(arr[idx - 2] - arr[idx - 1])
        arr = arr[::-1]
        shuffle_order = np.array([(21 * x) % 55 - 1 for x in range(54, -1, -1)], dtype=int)
        arr = arr[shuffle_order]
        shuffle_order = [(x + 31) % 55 for x in range(55)]
        for _ in range(4):
            for idx in range(55):
                arr[idx] = self.__bound_int(arr[idx] - arr[shuffle_order[idx]])
        return arr

    def __bound_int(self, value: int):
        return value if value > 0 else value + self.BIG_INT
