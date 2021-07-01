# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2021-07-01
Describe: FFT and iFFT
"""

import math
import operator
from functools import reduce
import numpy as np


class FFT:
    def __init__(self, n_set: list, is_ifft=False):
        self.point_n = self.prod(n_set)
        self.set_l = len(n_set)
        self.n_set = n_set
        self.pre_n_set = [1] + n_set
        self.is_ifft = is_ifft
        self.base_const = (0 + 1j) * -2 * math.pi
        if is_ifft:
            self.base_const = -self.base_const

    @staticmethod
    def prod(data):
        return reduce(operator.mul, data, 1)

    def generate_data(self):
        test_vec = np.random.randn(self.point_n) + 1j * np.random.randn(self.point_n)
        test_vec_mean = np.mean(np.abs(test_vec) ** 2)
        return test_vec / test_vec_mean

    def fft(self):
        origin_data = self.generate_data()
        if not self.is_ifft:
            np_result = np.fft.fft(origin_data)
        else:
            np_result = np.fft.ifft(origin_data)

        for i, radix_size in enumerate(self.n_set):
            group_size = int(self.point_n / self.prod(self.n_set[i:]))
            span = int(self.point_n / self.prod(self.n_set[:i + 1]))
            inter_data = list(np.zeros(self.point_n))

            n_radix = span
            W = self.prod(self.pre_n_set[:i + 1]) / self.point_n
            const = self.base_const * W
            for i_radio in range(n_radix):
                twiddle = list(map(lambda x: np.exp(const * x * i_radio), range(radix_size)))

                for offset_in_group in range(group_size):
                    load_index = slice(i_radio * group_size + offset_in_group, self.point_n, span * group_size)
                    args = origin_data[load_index]
                    if not self.is_ifft:
                        results = np.fft.fft(args)
                    else:
                        results = np.fft.ifft(args)
                    tw_results = list(map(lambda x, y: x * y, results, twiddle))
                    write_index = slice(offset_in_group + i_radio * group_size * radix_size,
                                        offset_in_group + (i_radio + 1) * group_size * radix_size,
                                        group_size)
                    inter_data[write_index] = tw_results
            origin_data = np.array(inter_data)

        return 10 * math.log10(np.mean(np.abs(origin_data - np_result) ** 2) / np.mean(np.abs(origin_data) ** 2))


if __name__ == '__main__':
    f = FFT([2, 4, 3, 5])
    evm = f.fft()
    print(evm)
    f = FFT([2, 4, 3, 5], True)
    evm = f.fft()
    print(evm)
