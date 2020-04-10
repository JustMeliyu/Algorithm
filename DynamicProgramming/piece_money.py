# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-09
Describe:
凑钱
给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，
再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1
给若干1，2，5，10面额的钱，将它们凑成一个总额amount

"""

from tools.common import get_func_time
import sys
sys.setrecursionlimit(9000000)  # 递归这里设置大一些


class Solution:

    def __init__(self, coins=None):
        if coins is None:
            coins = [1, 2, 5, 10, 100]
        self.change = coins
        self.case = {}

    def change_money(self, money, index=0):
        """
        给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，
        再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1
        给若干1，2，5，10面额的钱，将它们凑成一个总额amount
        存在self.change[index]的分解+不存self.change[index]的分解
        :param money    需要拆分的现金
        :param index    用于指示拆分情况
        """
        if money == 0:
            return 1
        if money < 0 or index >= len(self.change):
            return 0
        return self.change_money(money - self.change[index], index) + \
               self.change_money(money, index + 1)

    def change_money2(self, money):
        """
        给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，
        如果不可能凑出，算法返回 -1
        F(amount) = min(F(amount - c1) + 1, F(amount - c2) + 1, ..., F(amount - ck) + 1)
        """
        if money < 0:
            return -1
        if money == 0:
            return 0
        min_coins = float('inf')
        for coin in self.change:
            if self.case.get(money - coin) is None:
                self.case[money - coin] = self.change_money2(money - coin)
            if self.case[money - coin] < 0:
                continue
            min_coins = min(self.case[money - coin] + 1, min_coins)
        return min_coins

    @get_func_time
    def run(self, money, index=0):
        # return self.change_money(money, index)
        return self.change_money2(money)


if __name__ == '__main__':
    s = Solution()
    print(s.run(201))
