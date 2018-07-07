from unittest import TestCase

import numpy as np
from core.src.scenario import Scenario
from core.src.type import ShockType


class TestScenario(TestCase):
    def test_calculate_shock(self):
        scenario = Scenario(np.array(np.linspace(-1.0, 1.0, 10)))
        scenario_shock = scenario.calculate_shock(0.0, shock_type=ShockType.CHANGE)

        for idx in range(10):
            self.assertAlmostEqual(scenario.scenarios[idx], scenario_shock.scenarios[idx], 1e-12)

        pass

    pass
