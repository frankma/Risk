import numpy as np
from scipy.stats import norm, rankdata

from riskfactor.src.risk_factor_engine import RiskFactorEngine
from riskmath.src.utils import Utils, CSRandom, GenParetoDist


class RFETCopula(RiskFactorEngine):
    def __init__(self, num_path: int, co_dep_data_size: int, co_dep_data_shift: int, decay_rate: float,
                 left_percentile: float = 1.0, right_percentile: float = 99.0, seed: int = 99999,
                 dof: int = 4, num_draw: int = 30):
        super().__init__(num_path)

        self._co_dep_data_size = co_dep_data_size
        self._co_dep_data_shift = co_dep_data_shift
        self._decay_rate = decay_rate
        self._left_percentile = left_percentile
        self._right_percentile = right_percentile
        self._dof = dof
        self._num_draw = num_draw
        self._rand_num_gen = CSRandom(seed)
        # generate global variables
        self._co_dep_norms = self.__gen_co_dep_norms()
        self._t_indices = self.__gen_t_indices()
        self._chi_draws = self.__gen_chi_draws()
        self._draw_signs = self.__gen_draw_signs()

    def __gen_co_dep_norms(self):
        offset = 0.5 / self._co_dep_data_size
        percentiles = np.linspace(start=offset, stop=1.0 - offset, num=self._co_dep_data_size)
        return norm.ppf(percentiles)

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

    def generate_shuffle(self, co_dep_data: np.ndarray):
        if np.shape(co_dep_data) != (self._co_dep_data_size,):
            raise ValueError('expect data shape in %i' % self._co_dep_data_size)
        order = rankdata(co_dep_data, method='ordinal') - 1
        co_dep_data_normed = self._co_dep_norms[order]

        co_dep_draw = np.sum(co_dep_data_normed[self._t_indices].reshape((self._num_draw, self.num_path)), axis=0)
        co_dep_draw *= np.sqrt(self._num_draw) * self._draw_signs
        co_dep_draw /= self._chi_draws

        return rankdata(co_dep_draw, method='ordinal') - 1

    def generate_marginal_dist(self, time_series: np.ndarray):
        data = self.volatility_filer(time_series=time_series, decay_rate=self._decay_rate)
        vol_adj = np.std(data, ddof=1)
        data /= vol_adj

        shift = 0.5 / self.num_path
        percentiles = np.linspace(start=shift, stop=1.0 - shift, num=self.num_path) * 100.0

        left_idx = percentiles < self._left_percentile
        right_idx = percentiles > self._right_percentile
        mid_idx = np.logical_not(np.logical_or(left_idx, right_idx))

        marginal_dist = np.zeros(self.num_path)
        marginal_dist[left_idx] = self.model_left_tail(data, self._left_percentile, percentiles[left_idx])
        marginal_dist[right_idx] = self.model_right_tail(data, self._right_percentile, percentiles[right_idx])
        marginal_dist[mid_idx] = Utils.percentile(data, percentiles=percentiles[mid_idx])
        marginal_dist *= vol_adj

        return marginal_dist

    @staticmethod
    def volatility_filer(time_series: np.ndarray, decay_rate: float, volatility_floor: float = 1.0e-4):
        if decay_rate >= 1.0 or time_series.__len__() < 30:
            return time_series
        else:
            vol_flr = volatility_floor * np.std(time_series, ddof=1)
            vols = np.ones(np.shape(time_series)) * np.sqrt(np.average(np.square(time_series[0:28])))
            for idx in range(30, time_series.__len__()):
                roll_var = (1.0 - decay_rate) * (time_series[idx - 1] ** 2) + decay_rate * (vols[idx - 1] ** 2)
                vols[idx] = max(vol_flr, np.sqrt(roll_var))
            vol_terminal = np.sqrt((1.0 - decay_rate) * (time_series[-1] ** 2) + decay_rate * (vols[-1] ** 2))
            vol_filter = vols / max(vol_flr, vol_terminal)
            return time_series / vol_filter

    @staticmethod
    def model_left_tail(data: np.ndarray, left_percentile: float, percentiles_to_extract: np.ndarray):
        if np.any(percentiles_to_extract <= 0.0) or np.any(percentiles_to_extract >= left_percentile):
            raise ValueError('the percentile should be bound by (0.0, %.f) exclusively' % left_percentile)
        u_array = percentiles_to_extract / left_percentile  # u \in (0.0, 1.0)

        cutoff = Utils.percentile(data, [left_percentile])[0]
        tail = data[data < cutoff]
        model = GenParetoDist.fit_given_loc(x_array=tail, loc=cutoff)

        return model.ppf(u_array=u_array)

    @staticmethod
    def model_right_tail(data: np.ndarray, right_percentile: float, percentiles_to_extract: np.ndarray):
        if np.any(percentiles_to_extract <= right_percentile) or np.any(percentiles_to_extract >= 100.0):
            raise ValueError('the percentile should be bound by (%.f, 100.0) exclusively' % right_percentile)
        u_array = (percentiles_to_extract - right_percentile) / (100.0 - right_percentile)  # u \in (0.0, 1.0)

        cutoff = Utils.percentile(data, [right_percentile])[0]
        tail = data[data > cutoff]
        model = GenParetoDist.fit_given_loc(x_array=tail, loc=cutoff)

        return model.ppf(u_array=u_array)
