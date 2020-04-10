# -*- coding: utf-8 -*- 
"""
__author__ = "Road36"
__date__ = "19-10-17"
Describe:
https://leetcode-cn.com/problems/first-missing-positive/

给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""
from typing import List


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        min_num = None
        is_serial = False

        nums = sorted(nums)
        i = 0
        for index, i in enumerate(nums):
            if not is_serial:
                if i <= 0:
                    continue
                if not min_num:
                    if i != 1:
                        return 1
                    min_num = i
                    continue

                if i - min_num == 1 or i == min_num:
                    is_serial = True
                    min_num = i
                else:
                    return min_num + 1
            else:
                if i - min_num == 1 or i == min_num:
                    min_num = i
                    continue
                return min_num + 1

        return i + 1 if min_num else 1

    @staticmethod
    def firstMissingPositive2(nums: List[int]) -> int:
        if nums is None or nums.__len__() == 0:
            return 1

        l = nums.__len__()
        for i in range(0, l):
            if nums[i] < 0 or nums[i] > l:
                nums[i] = 0
        for i in range(0, l):
            if nums[i] != 0:
                nums[(nums[i] - 1) % l] += 2 * l
        # print(nums)
        for i in range(0, l):
            if nums[i] <= l:
                return i + 1
        return l + 1

        # for i in nums:
        #     if i <= 0:
        #         continue
        #
        #     if not min_num:
        #         min_num = i
        #     else:
        #         if i <= min_num:
        #             min_num = i
        #
        # if is_serial:
        #     if min_num == 1:
        #         return second_num + 1
        #     else:
        #         return min_num - 1
        # else:
        #     if min_num == 1:
        #         return min_num + 1
        #     else:
        #         if min_num:
        #             return min_num - 1
        #         else:
        #             return 1


if __name__ == '__main__':
    print(Solution.firstMissingPositive([-5]))
