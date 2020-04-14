# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-14
Describe:
归并算法
采用分治算法，将问题分成一些小的问题，然后递归求解，而治则是将每个阶段的得到的答案组合在一起
https://www.cnblogs.com/chengxiao/p/6194356.html
"""
from tools.common import get_func_time
from typing import List
import copy


class Solution:

    @get_func_time
    def merge_sort(self, arr: List[int]) -> List[int]:
        tmp = copy.copy(arr)

        def sort_arr(array, start, end, tmp_arr):
            if start == end:
                return

            mid = int((end + start) / 2)
            sort_arr(array, start, mid, tmp_arr)
            sort_arr(array, mid + 1, end, tmp_arr)
            merge(array, start, mid, end, tmp_arr)

        def merge(array, start, mid, end, tmp_arr):
            i = start
            j = mid + 1
            for k in range(start, end+1):
                if j > end:
                    tmp_arr[k:end+1] = array[i:end+1]
                    break
                elif i > mid:
                    tmp_arr[k:end+1] = array[j:end+1]
                    break
                elif array[j] >= array[i]:
                    tmp_arr[k] = array[i]
                    i += 1
                else:
                    tmp_arr[k] = array[j]
                    j += 1

            array[start:end+1] = tmp_arr[start:end+1]
        sort_arr(arr, 0, len(arr) - 1, tmp)

        return arr


if __name__ == '__main__':
    st = Solution()
    # a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222]
    a = [3, 40, 7, 34, 2, 89, 1, 432, 23, 89, 5, 2222] * 10
    # a = [3, 40, 7, 34]
    print(st.merge_sort(a))
