import numpy as np

from core.src.scenario import Scenario
from core.src.type import ShockType


class TimeSeries(object):
    def __init__(self, time_series: np.ndarray):
        self._time_series = time_series
        pass

    def calculate_time_step_shocks(self, shock_type: ShockType):
        if shock_type.__eq__(ShockType.ARITHMETIC):
            return Scenario(self._time_series[1:] / self._time_series[:-1] - 1.0)
        elif shock_type.__eq__(ShockType.CHANGE):
            return Scenario(self._time_series[1:] - self._time_series[:-1])
        else:
            raise NotImplemented('method %s not implemented yet' % shock_type.value)
        pass

    @staticmethod
    def restore_time_series(base: float, shocks: Scenario, shock_type: ShockType):
        time_series = np.ones(shocks.num_scen + 1, dtype=float) * base
        if shock_type.__eq__(ShockType.ARITHMETIC):
            for idx in range(1, time_series.size):
                time_series[idx] = time_series[idx - 1] * (1.0 + shock_type[idx - 1])
        elif shock_type.__eq__(ShockType.CHANGE):
            for idx in range(1, time_series.size):
                time_series[idx] = time_series[idx - 1] + shock_type[idx - 1]
        else:
            raise NotImplemented('method %s not implemented yet' % shock_type.value)

        return TimeSeries(time_series)

    pass
