# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-14
Describe:
给定一个只包含大写英文字母的字符串S，求该字符串的所有可能队列组合数
ABA, 所有可能 ABA, AAB, BAA
"""
from typing import List
from tools.common import get_func_time


class Permutation:

    def __init__(self):
        self.count = 0
        self.tmp = []
        self.re = []
        self.min = float('inf')

    def permutation_count(self, varchar: str):
        # 全排列
        array = set()
        _l = len(varchar) - 1

        def count(s, start, arr: set):
            if start == _l:
                arr.add(s)
                return
            for i in range(start, _l+1):
                if i != start:
                    # 求从i之后的字符，有多少排列组合可能
                    s = s[:start] + s[i] + s[start+1:i] + s[start] + s[i+1:]
                count(s, start + 1, arr)
                if i != start:
                    # 交换回来之前的字符串
                    s = s[:start] + s[i] + s[start+1:i] + s[start] + s[i+1:]

        count(varchar, 0, array)
        return len(array)

    @get_func_time
    def combination_count(self, array: List[int]):
        # 从10个数抽取三个数有多少组合
        def calculate(arr, _min):
            v = arr[0] * arr[0] + arr[0] * arr[1] - arr[1] * arr[1] + arr[2]
            return min(v, _min)

        def combination(arr, tmp, _min):
            for i in range(len(arr)):
                if len(tmp) == 2:
                    tmp.append(arr[i])
                    _min = calculate(tmp, _min)
                    tmp.pop(-1)
                else:
                    tmp.append(arr[i])
                    _min = combination(arr[:i] + arr[i+1:], tmp, _min)
                    tmp.pop(-1)
            return _min
        self.min = combination(array, self.tmp, self.min)


if __name__ == '__main__':
    p = Permutation()
    # char = "ABA"
    char = "ABCDEFGHHA"
    # print(p.permutation_count(char))
    a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3] * 10
    # a = [1, 1, 3, 4]
    p.combination_count(a)
    print(p.count)
    print(p.min)
