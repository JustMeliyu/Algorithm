# -*- coding: utf-8 -*- 
"""
__author__ = "Road36"
__date__ = "19-12-2"
Describe:
随机给10个整数, 从其中随机抽选3个, 求 x^2 + x*y - y^2 + z 的最小值, 给定整数范围在-512-512之间
https://blog.csdn.net/weixin_39971186/article/details/103315477
"""
import sys
import os
from importlib import reload
current_path = os.getcwd()
sys.path.append(current_path)
reload(sys)
from typing import List
import itertools
from tools.common import get_func_time

sys.setrecursionlimit(9000000)  # 这里设置大一些


class Solution:
    def __init__(self):
        self.min = float('inf')

    @get_func_time
    def min_value1(self, numbers: List[int]):
        # 使用迭代器
        for x, y, z in itertools.permutations(numbers, 3):
            self.min = min(self.min, x * x + x * y - y * y + z)
        return self.min

    @get_func_time
    def min_value2(self, numbers: List):
        # 普通遍历
        for i, x in enumerate(numbers):
            for j, y in enumerate(numbers):
                if i == j:
                    continue
                for m, z in enumerate(numbers):
                    if i == m or j == m:
                        continue
                    self.min = min(self.min, x * x + x * y - y * y + z)
        return self.min

    @get_func_time
    def min_value3(self, numbers: List):
        # 回溯算法
        def _min_value(my_nums: List[int], use_num: List[int], _min):
            if len(my_nums) == 3:
                v = my_nums[0] * my_nums[0] + my_nums[0] * my_nums[1] - my_nums[1] * my_nums[1] + my_nums[2]
                _min = min(_min, v)
                return _min, []

            for i in range(len(use_num)):
                my_nums.append(i)
                _min, my_nums = _min_value(my_nums, numbers[:i] + numbers[i+1:], _min)
            # return _min, my_nums
        self.min, z = _min_value([], numbers, float('inf'))
        return self.min

    @classmethod
    def array(cls, numbers: List, num: int):
        # 实现排列
        return [_i for _i in itertools.permutations(numbers, num)]

    @classmethod
    def combination(cls, numbers: List, num: int):
        # 实现组合
        return [_i for _i in itertools.combinations(numbers, num)]


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [0 for i in range(len(nums))]
        ans = []
        def perm(res, cur):
            if cur == 3:
                ans.append(res[:])
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = 1
                        res[cur] = nums[i]
                        perm(res, cur+1)
                        used[i] = 0
        perm([0 for i in range(len(nums))], 0)
        return ans


if __name__ == '__main__':
    # a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 3] * 10
    a = [1, -1, 2, -2, 2, 3, -4, 0, 5, 3]
    # a = [1, 1, 1]

    s = Solution()
    # print(s.min_value1(a))
    print(s.min_value2(a))
    # print(s.min_value3(a))

    # print([i for i in range(1000)])
    ss = Solution2()
    # print(ss.permute(a))
