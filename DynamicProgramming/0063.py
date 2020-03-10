# -*- coding: utf-8 -*- 
"""
__author__ = "Road36"
__date__ = "20-3-10"
Describe:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
https://leetcode-cn.com/problems/unique-paths-ii
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """"""
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [[0] * n for _i in range(m)]

        # 时间复杂度 O(n )
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                result[i][0] = 1
            else:
                break

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                result[0][i] = 1
            else:
                break

        for i in range(1, m):  # 逐行
            for j in range(1, n):  # 逐列
                # 存储以往结果，并使用以往结果
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    result[i][j] = (result[i - 1][j] if obstacleGrid[i - 1][j] == 0 else 0) + (
                        result[i][j - 1] if obstacleGrid[i][j - 1] == 0 else 0)
        return result[-1][-1]


if __name__ == '__main__':
    s = Solution()
    d = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # d = [
    #     [0, 0],
    #     [1, 1],
    #     [0, 0]
    # ]
    # d = [
    #     [0],
    #     [1]
    # ]
    print(s.uniquePathsWithObstacles(d))
