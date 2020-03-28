# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-25
Describe:
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List


class Solution:
    def max_profit(self, prices: List) -> int:
        max_value = 0
        for i, v in enumerate(prices[:-1]):
            max_value = max(max_value, max(prices[i + 1:]) - v)
        return max_value

    def max_profit2(self, prices: List) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices[1:]:
            if i > min_price:
                max_profit = max(max_profit, i - min_price)
            else:
                min_price = i
        return max_profit


if __name__ == '__main__':
    s = Solution()
    p = [7, 1, 5, 3, 6, 4]
    print(s.max_profit2(p))