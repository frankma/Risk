import numpy as np


class Sensitivity(object):
    def __init__(self):
        pass

    @staticmethod
    def calculate_taylor_coefficients(orders: list):
        coefficients = np.ones(orders.__len__())
        return coefficients

    pass
