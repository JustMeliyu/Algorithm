# -*- coding: utf-8 -*- 

"""
Author: Anger36
Date: 19-5-17
Describe: 爬楼梯
一共有10级楼梯, 每次只能走1步或者2步, 爬上这个楼梯一共需要多少种方式
"""
import sys
from tools.common import get_func_time, run_mothod
sys.setrecursionlimit(10000)    # 增加递归次数


class Solution(object):
    def __init__(self):
        self.count = 0

    def climb_stairs(self, step: int):
        """
        时间复杂度: O(2^N), 空间复杂度: O(1)
        :param step:
        :return:
        """
        self.count += 1
        if step == 1:
            return 1
        if step == 2:
            return 2
        return self.climb_stairs(step - 1) + self.climb_stairs(step - 2)

    def climb_stairs2(self, step: int, dic: dict):
        """
        时间复杂度: O(N), 空间复杂度O(N)
        :param step:
        :param dic: 存储每一阶的信息
        :return:
        """
        if step == 1:
            return 1
        if step == 2:
            return 2
        if dic.get(step) is not None:
            value = dic.get(step)
        else:
            self.count += 1
            value = self.climb_stairs2(step - 1, dic) + self.climb_stairs2(step - 2, dic)
            dic[step] = value
        return value

    def climb_stairs3(self, step: int):
        """
        时间复杂度: O(N), 空间复杂度O(1)
        :param step:
        :return:
        """
        a = 1
        b = 2
        if step == 1:
            return a
        if step == 2:
            return b
        t = 3
        while t <= step:
            self.count += 1
            b, a = a + b, b
            t += 1
        return b


if __name__ == '__main__':
    info = {}
    s = Solution()
    run_mothod(s.climb_stairs2, 1000, info)
    run_mothod(s.climb_stairs3, 1000)
