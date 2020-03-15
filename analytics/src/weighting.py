from enum import Enum

import numpy as np

class WeightType(Enum):
    HARREL_DAVIS: 1
    SINGULAR: 2
    AVERAGE: 3
    LEFTWARD_AVG: 4
    RIGHTWARD_AVG: 5


class Weighting(object):
    def __init__(self, sample_size: int, weight_type: WeightType, percentile: float):
        self._sample_size = sample_size
        self._weight_type = weight_type
        self._percentile = percentile
        if percentile <= 0.0 or percentile >= 100.0:
            raise Exception('percentile need to between [0.0, 100.0], received %f' % percentile)
        pass

    def calc_weights(self) -> np.ndarray:
        pass

    def __eq__(self, other):
        equals = False
        if isinstance(other, Weighting):
            equals = self._sample_size.__eq__(other._sample_size) \
                     and self._weight_type.__eq__(other._weight_type) \
                     and self._percentile.__eq__(other._percentile)
        return equals

    def __str__(self):
        return '%i-%s-%f' % (self._sample_size, self._weight_type.__str__(), self._percentile)

    def __hash__(self):
        return self.__str__().__hash__()

    @staticmethod
    def calc_harrel_davis_weights(sample_size: int, percentile: float, integral_steps: int = 100):
        num_intervals = sample_size * integral_steps
        step = float(1.0 / num_intervals)
        left_bound = (sample_size + 1) * percentile / 100.0 - 1.0
        right_bound = (sample_size + 1) * (1 - percentile) / 100.0 - 1.0

        xs = np.linspace(0, )

        pass

    pass
