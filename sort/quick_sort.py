# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-14
Describe:
快速排序

https://www.cnblogs.com/chengxiao/p/6194356.html
"""

from tools.common import get_func_time


class QuickSort:

    @get_func_time
    def quick_sort1(self, array):
        """
        传统快排
        """
        def quick_sort(arr, start, end):
            if start >= end:
                return
            i = start
            j = end
            pivot = arr[i]
            while i < j:
                # 从第j个元素向前, 依次与pivot比较, 当出现比它小的时候, 停止,
                while arr[j] >= pivot and i < j:
                    j -= 1

                # 此时将此时的第j个元素赋值给第i个元素
                arr[i] = arr[j]

                # 从第i个元素向后, 依次与pivot比较, 当出现比它大的时候, 停止,
                while arr[i] <= pivot and i < j:
                    i += 1

                # 此时将此时的第i个元素赋值给第j个元素
                arr[j] = arr[i]

            # 当i与j相等时, 将povit赋值给第i个元素
            arr[i] = pivot
            # 递归前半区
            quick_sort(arr, start, i - 1)
            # 递归后半区
            quick_sort(arr, j + 1, end)
        quick_sort(array, 0, len(array) - 1)
        return array

    def quick_sort2(self, my_list):
        if len(my_list) > 1:
            # 选择第一个元素做基准数(pivot)
            povit = my_list[0]
            left = []
            right = []
            for i in my_list[1:]:
                if i < povit:
                    # 将小的放到一个数组
                    left.append(i)
                else:
                    # 大的放到另一个数组
                    right.append(i)
            # 再分别递归两个数组, 将所有数组相加
            return self.quick_sort2(left) + [povit] + self.quick_sort2(right)
        else:
            return my_list


if __name__ == "__main__":
    # a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222] * 10
    # a = [3, 40, 7, 34]
    qs = QuickSort()
    print(qs.quick_sort1(a))
