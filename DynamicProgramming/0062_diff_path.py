# -*- coding: utf-8 -*-

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

https://leetcode-cn.com/problems/unique-paths/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[1] * n] * m  # 存储到达每一个位置的路径数
        # 时间复杂度 O(n )
        for i in range(1, m):  # 逐行
            for j in range(1, n):  # 逐列
                # 存储以往结果，并使用以往结果
                result[i][j] = result[i - 1][j] + result[i][j - 1]
        return result[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
