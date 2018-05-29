from riskfactor.src.risk_engine import RiskEngine
from riskmath.src.cs_random import CSRandom


class RiskEngineTCopula(RiskEngine):
    def __init__(self, n_path: int):
        self.n_path = n_path
        pass
