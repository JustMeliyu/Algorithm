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


class Solution:
    def __init__(self):
        self.remaining = {}
        self.pro_index = [(0, 0)]
        for i in range(9):
            for j in range(9):
                self.remaining[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def solve_sudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                b = board[i]
                if board[i][j] == ".":
                    while self.remaining[(i, j)]:
                        if self.remaining[(i, j)][0] not in board[i]:
                            board[i][j] = self.remaining[(i, j)][0]
                            if self.judge_repeat(board, i, j):
                                self.pro_index.append((i, j))
                                break
                        del self.remaining[(i, j)][0]
                    else:
                        self.remaining[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                        while not self.remaining[self.pro_index[-1]]:
                            board[self.pro_index[-1][0]][self.pro_index[-1][1]] = "."
                            del self.pro_index[-1]

                        del self.remaining[self.pro_index[-1]][0]
                        board[i][j] = "."
                        board[self.pro_index[-1][0]][self.pro_index[-1][1]] = "."
                        del self.pro_index[-1]
                        self.solve_sudoku(board)
                        break

    @classmethod
    def judge_repeat(cls, board: list, i: int, j: int):
        tmp = []
        for q in range(9):
            if board[q][j] in tmp:
                return False
            if board[q][j] != ".":
                tmp.append(board[q][j])
        a = i // 3
        b = j // 3
        tmp2 = []
        for m in range(a * 3, a * 3 + 3):
            for n in range(b * 3, b * 3 + 3):
                if board[m][n] in tmp2:
                    return False
                if board[m][n] != ".":
                    tmp2.append(board[m][n])
        return True


if __name__ == '__main__':
    sudoku = [
        [5, 3, ".", ".", 7, ".", ".", ".", "."],
        [6, ".", ".", 1, 9, 5, ".", ".", "."],
        [".", 9, 8, ".", ".", ".", ".", 6, "."],
        [8, ".", ".", ".", 6, ".", ".", ".", 3],
        [4, ".", ".", 8, ".", 3, ".", ".", 1],
        [7, ".", ".", ".", 2, ".", ".", ".", 6],
        [".", 6, ".", ".", ".", ".", 2, 8, "."],
        [".", ".", ".", 4, 1, 9, ".", ".", 5],
        [".", ".", ".", ".", 8, ".", ".", 7, 9]
    ]
    s = Solution()
    s.solve_sudoku(sudoku)
    print(sudoku)

    # v = {(1, 3): "10000000000"}
    # print(v[(1, 3)])
