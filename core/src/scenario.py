import numpy as np

from core.src.type import ShockType


class Scenario(object):
    def __init__(self, scenarios: np.ndarray):
        self.scenarios = scenarios
        self.num_scenarios = np.size(self.scenarios)
        pass

    def clone(self):
        scenarios_clone = np.copy(self.scenarios)
        return Scenario(scenarios_clone)

    def apply_shock(self, base: float, shock_type: ShockType):
        if shock_type == ShockType.ARITHMETIC:
            self.scenarios /= base
            self.scenarios -= 1.0
        elif shock_type == ShockType.LOG:
            self.scenarios = np.log(self.scenarios / base)
        elif shock_type == ShockType.CHANGE:
            self.scenarios -= base
        else:
            raise NotImplemented('method %s not implemented yet' % shock_type.value)
        pass

    def reverse_shock(self, base: float, shock_type: ShockType):
        if shock_type == ShockType.ARITHMETIC:
            self.scenarios += 1.0
            self.scenarios *= base
        elif shock_type == ShockType.LOG:
            self.scenarios = np.exp(self.scenarios) * base
        elif shock_type == ShockType.CHANGE:
            self.scenarios += base
        else:
            raise NotImplemented('method %s not implemented yet' % shock_type.value)
        pass

    def calculate_shock(self, base: float, shock_type: ShockType):
        scenarios_copy = self.clone()
        scenarios_copy.apply_shock(base, shock_type)
        return scenarios_copy

    def calculate_level(self, base: float, shock_type: ShockType):
        scenarios_copy = self.clone()
        scenarios_copy.reverse_shock(base, shock_type)
        return scenarios_copy

    pass
