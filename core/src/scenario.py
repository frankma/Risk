import numpy as np

from core.src.type import ShockType


class Scenario(object):
    def __init__(self, scenarios: np.ndarray):
        self._scenarios = scenarios
        pass

    def clone(self):
        scenarios_clone = np.copy(self._scenarios)
        return Scenario(scenarios_clone)

    def apply_shock(self, base: float, shock_type: ShockType):
        if shock_type.__eq__(ShockType.ARITHMETIC):
            self._scenarios /= base
            self._scenarios -= 1.0
        elif shock_type.__eq__(ShockType.CHANGE):
            self._scenarios -= base
        else:
            raise NotImplemented('method not implemented yet')

    def calculate_shock(self, base: float, shock_type: ShockType):
        scenarios_copy = self.clone()
        return scenarios_copy.apply_shock(base, shock_type)
        pass

    pass
