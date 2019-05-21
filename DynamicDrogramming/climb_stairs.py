# -*- coding: utf-8 -*- 

"""
Author: Anger36
Date: 19-5-17
Describe: 爬楼梯
一共有10级楼梯, 每次只能走1步或者2步, 爬上这个楼梯一共需要多少种方式
"""
import sys
from tools.common import run_method
from tools.logger import logger
from functools import lru_cache
sys.setrecursionlimit(10000)    # 增加递归次数


class Solution(object):
    def __init__(self):
        self.count = 0

    def climb_stairs(self, step):
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

    def climb_stairs2(self, step, dic):
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

    def climb_stairs3(self, step):
        """
        时间复杂度: O(N), 空间复杂度O(1)
        :param step:
        :return:
        """

        if step == 1:
            return 1
        if step == 2:
            return 2
        a = 1
        b = 2
        for i in range(step - 2):
            self.count += 1
            b, a = a + b, b
        return b

    @lru_cache(10**8)
    def climb_stairs4(self, step):
        self.count += 1
        if step == 1:
            return 1
        elif step == 2:
            return 2
        else:
            return self.climb_stairs4(step - 1) + self.climb_stairs4(step - 2)


if __name__ == '__main__':
    info = {}
    s = Solution()
    run_method(s.climb_stairs, 20)
    logger.info(s.count)
    s.count = 0
    run_method(s.climb_stairs2, 1000, info)
    logger.info(s.count)
    s.count = 0
    run_method(s.climb_stairs3, 1000)
    logger.info(s.count)
    s.count = 0
    run_method(s.climb_stairs4, 1000)
    logger.info(s.count)
    s.count = 0
