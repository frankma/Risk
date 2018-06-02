import numpy as np

from riskfactor.src.risk_factor_engine import RiskFactorEngine
from riskmath.src.utils import CSRandom, Utils


class RiskFactorEngineTCopula(RiskFactorEngine):
    def __init__(self, num_path: int, co_dep_data_size: int, co_dep_data_shift: int, decay_rate: float,
                 seed: int = 99999, dof: int = 4, num_draw: int = 30):
        super().__init__(num_path)
        self._co_dep_data_size = co_dep_data_size
        self._co_dep_data_shift = co_dep_data_shift
        self._decay_rate = decay_rate
        self._rand_num_gen = CSRandom(seed)
        self._dof = dof
        self._num_draw = num_draw
        # generate global variables
        self._t_indices = self.__gen_t_indices()
        self._chi_draws = self.__gen_chi_draws()
        self._draw_signs = self.__gen_draw_signs()

    def __gen_t_indices(self):
        rands = self._rand_num_gen.next_uniform(self.num_path * self._num_draw)
        t_indices = rands.__mul__(self._co_dep_data_size).__add__(self._co_dep_data_shift).astype(int)
        return t_indices % self._co_dep_data_size

    def __gen_chi_draws(self):
        rands = self._rand_num_gen.next_uniform(self.num_path * 2 * self._dof).reshape((self.num_path * self._dof, 2))
        chi_sq = np.sqrt(-2.0 * np.log(rands[:, 0])) * np.cos(2.0 * np.pi * rands[:, 1])
        chi_sq **= 2
        chi_sq = np.sum(chi_sq.reshape(self._dof, self.num_path), axis=0)
        return np.sqrt(self._dof * chi_sq)

    def __gen_draw_signs(self):
        draw_sign = np.ones(self.num_path)
        draw_sign[1::2] *= -1
        return draw_sign

    def generate_rank(self, co_dep_data: np.ndarray):
        if np.shape(co_dep_data) != (self._co_dep_data_size,):
            raise ValueError('expect data shape in %i' % self._co_dep_data_size)
        co_dep_draw = np.sum(co_dep_data[self._t_indices].reshape((self._num_draw, self.num_path)), axis=0)
        co_dep_draw *= np.sqrt(self._num_draw) * self._draw_signs
        co_dep_draw /= self._chi_draws

        temp = co_dep_draw.argsort()
        rank = np.empty_like(temp)
        rank[temp] = np.arange(co_dep_draw.__len__())
        return rank

    def generate_marginal_dist(self, time_series: np.ndarray):
        time_series_vol_adj, vol = RiskFactorEngineTCopula.volatility_filer(time_series, self._decay_rate)
        vol_adj = np.std(time_series_vol_adj)
        percentiles = [x * 100 for x in np.linspace(0.5 / self.num_path, 1.0 - 0.5 / self.num_path, num=self.num_path)]
        marginal_dist = Utils.percentile(time_series_vol_adj / vol_adj, percentiles=percentiles)
        return marginal_dist
        pass

    @staticmethod
    def volatility_filer(time_series: np.ndarray, decay_rate: float, volatility_floor: float = 1.0e-4):
        if decay_rate >= 1.0 or time_series.__len__() < 30:
            return time_series, np.std(time_series, ddof=1)
        else:
            vol_flr = volatility_floor * np.std(time_series, ddof=1)
            vols = np.ones(np.shape(time_series)) * np.sqrt(np.average(np.square(time_series[0:28])))
            for idx in range(30, time_series.__len__()):
                roll_var = (1.0 - decay_rate) * (time_series[idx - 1] ** 2) + decay_rate * (vols[idx - 1] ** 2)
                vols[idx] = max(vol_flr, np.sqrt(roll_var))
            vol_terminal = np.sqrt((1.0 - decay_rate) * (time_series[-1] ** 2) + decay_rate * (vols[-1] ** 2))
            vol_filter = vols / max(vol_flr, vol_terminal)
            return time_series / vol_filter, np.average(vols)
