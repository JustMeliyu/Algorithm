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


def solve_sudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    for i in range(9):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if board[i][j] == ".":
                pass
            else:
                a.remove(board[i][j])


if __name__ == '__main__':
    sudoku = [
        [5, 3, ".", ".", 7, ".", ".", ".", "."],
        [6, ".", ".", 1, 9, 5, ".", ".", "."],
        [".", 9, 8, "", ".", ".", ".", 6, "."],
        [8, ".", ".", ".", 6, ".", ".", ".", 3],
        [4, ".", ".", 8, ".", 3, ".", ".", 1],
        [7, ".", ".", ".", 2, ".", ".", ".", 6],
        [".", 6, ".", ".", ".", ".", 2, 8, "."],
        [".", ".", ".", 4, 1, 9, ".", ".", 5],
        [".", ".", ".", ".", 8, ".", ".", 7, 9]
    ]
    solve_sudoku(sudoku)
