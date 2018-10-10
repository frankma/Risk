import numpy as np

from core.src.type import ShockType


class ScenarioVector(object):
    def __init__(self, scenarios: np.ndarray, immutable: bool = True):
        self._scenarios = scenarios
        self._num_scenarios = np.size(self._scenarios)
        self._immutable = immutable
        pass

    def clone(self, immutable: bool = False):
        scenarios_clone = np.copy(self._scenarios)
        return ScenarioVector(scenarios_clone, immutable)

    def check_for_modify(self):
        if self._immutable:
            raise ValueError('cannot modify immutable scenario vector')
        pass

    def add_to_self(self, level_to_add):
        self.check_for_modify()
        if isinstance(level_to_add, ScenarioVector):
            self._scenarios += level_to_add._scenarios
        else:
            self._scenarios + level_to_add
        pass


    pass
