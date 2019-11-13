# -*-coding:utf-8-*-
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List
import operator


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums = list(set(nums))
        re = []
        if len(nums) < 3:
            return []
        # n^3
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i + 1:]):
                for k, v3 in enumerate(nums[i + j + 2:]):
                    if v1 + v2 + v3 == 0:
                        m = sorted([v1, v2, v3])
                        for n in re:
                            if operator.eq(n, m):
                                break
                        else:
                            re.append(m)

        return list(re)

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        re = []
        nums.sort()
        i = 0
        j = len(nums) - 1
        k = 1
        while k < j:
            while i < k < j and nums[i] < 0 < nums[j]:
                if nums[i] + nums[k] + nums[j] < 0:
                    i += 1
                elif nums[i] + nums[k] + nums[j] > 0:
                    j -= 1
                else:
                    for r in re:
                        if r == [nums[i], nums[k], nums[j]]:
                            i += 1
                            j -= 1
                            break
                    else:
                        re.append([nums[i], nums[k], nums[j]])
                        i += 1
                        j -= 1

            k += 1
            i = 0
            j = len(nums) - 1
        return re


if __name__ == '__main__':
    s = Solution()
    # aa = [-1, 0, 1, 2, -1, -4]
    aa = [0, 14, -7, 2, 7, 11, -9, 11, -12, 6, -10, -8, 9, -3, 7, -6, 3, 4, 14, -10, -8, 5, -1, 6, 12, 9, 12, -11, -15,
          -5, 5, 0, -6, 13, 9, 9, 10, 7, 5, 13, -2, 11, -10, -15, -15, 4, -14, -4, -15, 7, -7, -15, -3, 8, -2, -13, -6,
          -5, -9, -14, 5, 12, 1, 6, 2, -12, -8, -11, 10, 13, -13, -14, 1, 14, 8, 1, -4, 9, 4, -12, -6, 13, 10, 6, 6, -7,
          8, 7, 3, 7, 8, -15, -4, -14, -1, 13, -11, 6, -12, -15, 4, 12, 8, -10, 4, 1, -1, 7, -13, -12, 10, -4, 8, 6, 10,
          -1, 6, -5, 13, -13, 9, 6, -13, -10]
    aa = [3, 0, -2, -1, 1, 2]
    # aa = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # aa = [0, 0, 0, 0]
    # print(s.threeSum(aa))
    print(s.threeSum2(aa))
    # print(sorted([1, 2, -1]))
    x = set()
    # print(operator.eq([1,2], [2,1]))
    # print([1,2] == [1,2])
