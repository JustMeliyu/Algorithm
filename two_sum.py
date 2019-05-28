# -*-coding:utf-8-*- 

"""
Author: Road36
Date: 19-5-8
Describe:
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
from tools.common import get_func_time


@get_func_time
def two_sum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    print("result is null")
    return None, None


def two_sum2(nums, target):
    require_num = {}
    for index in range(len(nums)):
        if require_num.get(target - nums[index]) is not None:
            return require_num.get(target - nums[index]), index
        else:
            require_num[nums[index]] = index
    print("result is null")
    return None, None


if __name__ == '__main__':
    a = [2, 7, 11, 15]
    b = 13
    # a = [3, 2, 4]
    # b = 6
    result = two_sum1(a, b)
    print(result)
    result = two_sum2([2, 7, 11, 15], 9)
    print(result)
