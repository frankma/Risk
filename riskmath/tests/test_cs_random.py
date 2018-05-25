from unittest import TestCase

from riskmath.src.cs_random import CSRandom


class TestCSRandom(TestCase):
    seed = 99999
    rand = CSRandom(seed)
    print(rand.seed_array)
    pass
