# -*-coding:utf-8-*- 

"""
Author: Anger36
Date: 19-5-9
Describe:
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""
import sys
from tools.common import get_func_time
sys.setrecursionlimit(10000)    # 增加递归次数


class Solution:
    def __init__(self):
        self.remaining = {}
        self.pro_index = [(0, 0)]
        for i in range(9):
            for j in range(9):
                self.remaining[(i, j)] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.count = 0

    def solve_sudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(self.pro_index[-1][0], 9):
            for j in range(9):
                self.count += 1
                if board[i][j] == ".":
                    while self.remaining[(i, j)]:
                        if self.remaining[(i, j)][0] not in board[i]:
                            if self.judge_repeat(board, i, j):
                                board[i][j] = self.remaining[(i, j)][0]
                                del self.remaining[(i, j)][0]
                                self.pro_index.append((i, j))
                                break
                        del self.remaining[(i, j)][0]
                    else:
                        self.remaining[(i, j)] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

                        while not self.remaining[self.pro_index[-1]]:
                            self.remaining[self.pro_index[-1]] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                            board[self.pro_index[-1][0]][self.pro_index[-1][1]] = "."
                            del self.pro_index[-1]

                        board[self.pro_index[-1][0]][self.pro_index[-1][1]] = "."
                        del self.pro_index[-1]
                        self.solve_sudoku(board)
                        break

    def judge_repeat(self, board: list, i: int, j: int):
        for q in range(9):
            if board[q][j] == self.remaining[(i, j)][0]:
                return False
        a = i // 3
        b = j // 3
        for m in range(a * 3, a * 3 + 3):
            for n in range(b * 3, b * 3 + 3):
                if board[m][n] == self.remaining[(i, j)][0]:
                    return False
        return True


class Solution2:
    def __init__(self):
        self.fill_points = []

    def solveSudoku(self, board):
        fill_points = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    fill_points.append([i, j])

        def judge_repeat(index, value):
            for q in range(9):
                if board[fill_points[index][0]][q] == value:
                    return False
                if board[q][fill_points[index][1]] == value:
                    return False
            a = fill_points[index][0] // 3
            b = fill_points[index][1] // 3
            for m in range(a * 3, a * 3 + 3):
                for n in range(b * 3, b * 3 + 3):
                    if board[m][n] == value:
                        return False
            return True

        def fill_point(index):
            if index == len(fill_points):
                return True
            for v in range(1, 10):
                if judge_repeat(index, str(v)):
                    board[fill_points[index][0]][fill_points[index][1]] = str(v)
                    if fill_point(index + 1):
                        return True
                    board[fill_points[index][0]][fill_points[index][1]] = "."
            return False

        fill_point(0)


if __name__ == '__main__':

    @get_func_time
    def test():
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
        s = Solution2()
        s.solveSudoku(sudoku)
        print(sudoku)
        # print(s.count)

    test()

    # v = {(1, 3): "10000000000"}
    # print(v[(1, 3)])
