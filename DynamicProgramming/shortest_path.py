# -*- coding: utf-8 -*- 

"""
Author: Road36
Date: 19-5-20
Describe:
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
from tools.common import run_method
from tools.logger import logger


class Solution(object):
    def __init__(self):
        self.sum_info = {}

    @classmethod
    def get_rol_sum(cls, grid, row, col=0):
        result = 0
        for i in range(row + 1):
            result += grid[i][col]
        return result

    def min_path_sum(self, grid):
        row = len(grid) - 1
        col = len(grid[0]) - 1
        sum_info = {}

        def get_data(info, r, c):
            if sum_info.get((r, c)) is None:
                if r == 0:
                    sum_info[(r, c)] = sum(info[0][:c + 1])
                elif c == 0:
                    sum_info[(r, c)] = self.get_rol_sum(grid, r)
                else:
                    res = min(get_data(info, r, c - 1), get_data(info, r - 1, c))
                    sum_info[(r, c)] = res + info[r][c]
            return sum_info.get((r, c))
        result = get_data(grid, row, col)
        return result

    def min_path_sum3(self, grid, row, col):
        if self.sum_info.get((row, col)) is None:
            if row == 0:
                self.sum_info[(row, col)] = sum(grid[0][:col + 1])
            elif col == 0:
                self.sum_info[(row, col)] = self.get_rol_sum(grid, row)
            else:
                res = min(self.min_path_sum3(grid, row, col - 1), self.min_path_sum3(grid, row - 1, col))
                self.sum_info[(row, col)] = res + grid[row][col]
        return self.sum_info[(row, col)]

    def min_path_sum2(self, grid):
        row = len(grid)
        col = len(grid[0])
        if grid is None or row == 0:
            return 0
        is_rowmore = row >= col
        dp = [0] * (col if is_rowmore else row)

        # Base Case
        dp[0] = grid[0][0]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + (grid[0][i] if is_rowmore else grid[i][0])
        # 一般情况
        for i in range(1, max(row, col)):
            dp[0] = dp[0] + (grid[i][0] if is_rowmore else grid[0][i])
            for j in range(1, min(row, col)):
                dp[j] = min(dp[j - 1], dp[j]) + (grid[i][j] if is_rowmore else grid[j][i])
        return dp[-1]

    def min_path_sum4(self, grid):
        row, col = len(grid), len(grid[0])
        if row == col == 0:
            return 0
        for i in range(1, col):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, row):
            grid[j][0] += grid[j - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    # data = [[1,2],[1,1]]
    # data = [
    #     [1, 3, 1],
    #     [1, 5, 1],
    #     [4, 2, 1]
    # ]
    # data = [[1, 4, 8, 6, 2, 2, 1, 7],
    #         [4, 7, 3, 1, 4, 5, 5, 1],
    #         [8, 8, 2, 1, 1, 8, 0, 1],
    #         [8, 9, 2, 9, 8, 0, 8, 9],
    #         [5, 7, 5, 7, 1, 8, 5, 5],
    #         [7, 0, 9, 4, 5, 6, 5, 6],
    #         [4, 9, 9, 7, 9, 1, 9, 0]]
    data = [[7, 1, 3, 5, 8, 9, 9, 2, 1, 9, 0, 8, 3, 1, 6, 6, 9, 5],
            [9, 5, 9, 4, 0, 4, 8, 8, 9, 5, 7, 3, 6, 6, 6, 9, 1, 6],
            [8, 2, 9, 1, 3, 1, 9, 7, 2, 5, 3, 1, 2, 4, 8, 2, 8, 8],
            [6, 7, 9, 8, 4, 8, 3, 0, 4, 0, 9, 6, 6, 0, 0, 5, 1, 4],
            [7, 1, 3, 1, 8, 8, 3, 1, 2, 1, 5, 0, 2, 1, 9, 1, 1, 4],
            [9, 5, 4, 3, 5, 6, 1, 3, 6, 4, 9, 7, 0, 8, 0, 3, 9, 9],
            [1, 4, 2, 5, 8, 7, 7, 0, 0, 7, 1, 2, 1, 2, 7, 7, 7, 4],
            [3, 9, 7, 9, 5, 8, 9, 5, 6, 9, 8, 8, 0, 1, 4, 2, 8, 2],
            [1, 5, 2, 2, 2, 5, 6, 3, 9, 3, 1, 7, 9, 6, 8, 6, 8, 3],
            [5, 7, 8, 3, 8, 8, 3, 9, 9, 8, 1, 9, 2, 5, 4, 7, 7, 7],
            [2, 3, 2, 4, 8, 5, 1, 7, 2, 9, 5, 2, 4, 2, 9, 2, 8, 7],
            [0, 1, 6, 1, 1, 0, 0, 6, 5, 4, 3, 4, 3, 7, 9, 6, 1, 9]]
    s = Solution()
    # re = run_method(s.min_path_sum, data)
    # re = run_method(s.min_path_sum2, data)
    # re = run_method(s.min_path_sum3, data, len(data) - 1, len(data[0]) - 1)
    # re = run_method(s.min_path_sum4, data)
