from unittest import TestCase

from riskmath.src.cs_random import CSRandom


class TestCSRandom(TestCase):
    seed = 99999
    rand = CSRandom(seed)
    vec = rand.next_uniform(10)
    print(vec)
    pass
