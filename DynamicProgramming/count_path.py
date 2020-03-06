# -*- coding: utf-8 -*-

"""
求一个二维数组一个顶点到对角，一共有多少方式

"""


def count_path(m, n):
    result = [[1] * n] * m  # 存储到达每一个位置的路径数
    # 时间复杂度 O(n )
    for i in range(1, m):   # 逐行
        for j in range(1, n):   # 逐列
            # 存储以往结果，并使用以往结果
            result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[-1][-1]


if __name__ == '__main__':
    print(count_path(7, 3))
