import numpy as np
from scipy.stats import norm, rankdata

from riskengine.src.risk_engine import RiskEngine
from riskmath.src.utils import Utils, CSRandom, GenParetoDist


class RiskEngineTCopula(RiskEngine):
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

    def simulate(self, time_series: np.ndarray):
        pass

    def generate_shuffle_indices(self, co_dep_data: np.ndarray):
        if np.shape(co_dep_data) != (self._co_dep_data_size,):
            raise ValueError('expect co-dependent data shape in %i' % self._co_dep_data_size)
        data_order = self.__rank_array(array_to_rank=co_dep_data, force_unique=True)
        co_dep_data_normed = self._co_dep_norms[data_order]

        co_dep_draw = np.sum(co_dep_data_normed[self._t_indices].reshape((self._num_draw, self.num_path)), axis=0)
        co_dep_draw *= np.sqrt(self._num_draw) * self._draw_signs
        co_dep_draw /= self._chi_draws

        shuffle_indices = self.__rank_array(array_to_rank=co_dep_draw, force_unique=False)

        return shuffle_indices

    def adjust_time_series_volatility(self, time_series, volatility_floor: float = 1.0e-4, roll_window: int = 30):
        if self._decay_rate >= 1.0 or time_series.__len__() < roll_window:
            return time_series
        else:
            vol_flr = volatility_floor * np.std(time_series, ddof=1)
            vols = np.ones(np.shape(time_series)) * np.sqrt(np.average(np.square(time_series[0:28])))
            for idx in range(roll_window, time_series.__len__()):
                roll_var = (1.0 - self._decay_rate) * (time_series[idx - 1] ** 2) \
                           + self._decay_rate * (vols[idx - 1] ** 2)
                vols[idx] = max(vol_flr, np.sqrt(roll_var))
            vol_terminal = np.sqrt(
                (1.0 - self._decay_rate) * (time_series[-1] ** 2) + self._decay_rate * (vols[-1] ** 2))
            vol_filter = vols / max(vol_flr, vol_terminal)
            return time_series / vol_filter

    def generate_marginal_dist(self, time_series: np.ndarray):
        vol_adj = np.std(time_series, ddof=1)
        time_series /= vol_adj

        shift = 0.5 / self.num_path
        percentiles = np.linspace(start=shift, stop=1.0 - shift, num=self.num_path) * 100.0

        left_idx = percentiles < self._left_percentile
        right_idx = percentiles > self._right_percentile
        mid_idx = np.logical_not(np.logical_or(left_idx, right_idx))

        marginal_dist = np.zeros(self.num_path)
        marginal_dist[left_idx] = self.model_left_tail(time_series, self._left_percentile, percentiles[left_idx])
        marginal_dist[right_idx] = self.model_right_tail(time_series, self._right_percentile, percentiles[right_idx])
        marginal_dist[mid_idx] = Utils.percentile(time_series, percentiles=percentiles[mid_idx])
        marginal_dist *= vol_adj

        return marginal_dist

    @staticmethod
    def model_left_tail(data: np.ndarray, left_percentile: float, percentiles_to_extract: np.ndarray):
        if np.any(percentiles_to_extract <= 0.0) or np.any(percentiles_to_extract >= left_percentile):
            raise ValueError('the percentile should be bound by (0.0, %.f) exclusively' % left_percentile)
        u_array = percentiles_to_extract / left_percentile  # u \in (0.0, 1.0)

        cutoff = Utils.percentile(data, [left_percentile])[0]
        tail = data[data < cutoff]
        model = GenParetoDist.fit_given_loc(x_arr=tail, loc=cutoff)

        return model.ppf(u_arr=u_array)

    @staticmethod
    def model_right_tail(data: np.ndarray, right_percentile: float, percentiles_to_extract: np.ndarray):
        if np.any(percentiles_to_extract <= right_percentile) or np.any(percentiles_to_extract >= 100.0):
            raise ValueError('the percentile should be bound by (%.f, 100.0) exclusively' % right_percentile)
        u_array = (percentiles_to_extract - right_percentile) / (100.0 - right_percentile)  # u \in (0.0, 1.0)

        cutoff = Utils.percentile(data, [right_percentile])[0]
        tail = data[data > cutoff]
        model = GenParetoDist.fit_given_loc(x_arr=tail, loc=cutoff)

        return model.ppf(u_arr=u_array)

    @staticmethod
    def __rank_array(array_to_rank: np.ndarray, force_unique: bool = True):
        array = np.array(array_to_rank, dtype=float)
        if force_unique:
            array += np.linspace(0.0, 1e-16 * array.size, num=array_to_rank.size)
        return rankdata(array, method='ordinal') - 1

    pass
