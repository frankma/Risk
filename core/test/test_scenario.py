from unittest import TestCase

import numpy as np
from core.src.scenariovector import ScenarioVector


class TestScenario(TestCase):
    def test_create(self):
        sv = ScenarioVector(np.ones(10), immutable=False)
        sv.add_to_self(sv)
        pass

    pass
