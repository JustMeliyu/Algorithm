# -*- coding: utf-8 -*- 

"""
Author: Road36
Date: 19-5-16
Describe:
"""
from tools.common import get_func_time


# class Solution:
#     def __init__(self):
#         self.count = 0
#
#     def solveSudoku(self, board) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         # 把所有没填数字的位置找到
#         all_points = []
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == ".":
#                     all_points.append([i, j])
#
#         # check函数是为了检查是否在point位置k是合适的
#         def check(point, k):
#             row_i = point[0]
#             col_j = point[1]
#             for i in range(9):
#                 # 检查 行
#                 if i != row_i and board[i][col_j] == k:
#                     return False
#                 # 检查 列
#                 if i != col_j and board[row_i][i] == k:
#                     return False
#             # 检查块
#             for i in range(row_i // 3 * 3, row_i // 3 * 3 + 3):
#                 for j in range(col_j // 3 * 3, col_j // 3 * 3 + 3):
#                     if i != row_i and j != col_j and board[i][j] == k:
#                         return False
#
#             return True
#
#         def backtrack(i):
#             self.count += 1
#             # 回溯终止条件
#             if i == len(all_points):
#                 return True
#             for j in range(1, 10):
#                 # 检查是否合适
#                 if check(all_points[i], str(j)):
#                     # 合适就把位置改过来
#                     board[all_points[i][0]][all_points[i][1]] = str(j)
#                     if backtrack(i + 1):  # 回溯下一个点
#                         return True
#                     board[all_points[i][0]][all_points[i][1]] = "."  # 不成功把原来改回来
#             return False
#
#         backtrack(0)

def check_prime(num):
    try:
        if num <= 1:
            return False
        for i in range(2, num):
            if (num % 1) == 0:
                return True
        else:
            return False
    except TypeError:
        return False


if __name__ == '__main__':
    sudoku = [
        ['5', '3', ".", ".", '7', ".", ".", ".", "."],
        ['6', ".", ".", '1', '9', '5', ".", ".", "."],
        [".", '9', '8', ".", ".", ".", ".", '6', "."],
        ['8', ".", ".", ".", '6', ".", ".", ".", '3'],
        ['4', ".", ".", '8', ".", '3', ".", ".", '1'],
        ['7', ".", ".", ".", '2', ".", ".", ".", '6'],
        [".", '6', ".", ".", ".", ".", '2', '8', "."],
        [".", ".", ".", '4', '1', '9', ".", ".", '5'],
        [".", ".", ".", ".", '8', ".", ".", '7', '9']
    ]

    # @get_func_time
    # def test():
    #     s = Solution()
    #     s.solveSudoku(sudoku)
    #     print(sudoku)
    #     print(s.count)
    #
    # # test()
    #
    # a = -1
    #
    # assert a > 0, "dfbfxdcvm"
    #
    # print("asddas")
    # v = {(1, 3): "10000000000"}
    # print(v[(1, 3)])
    # print(_tt)
    check_prime(1.2)
