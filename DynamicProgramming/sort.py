# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-28
Describe:
某大学开学进行军训队列训练，将学生从一开始按顺序依次编号，并排成一行横队，
训练的规则如下：从头开始一至二报数，凡报到二的出列剩下的依次向前靠拢，再从头开始进行一至三报数，凡报到三的出列，剩下的依次向前靠拢，
继续从头开始进行一至二报数。。。以后每次从头开始轮流进行一至二报数、一至三报数直到剩下的人数不超过三人为止。
第一行为组数N，接着为N行学生人数，学生人数不超过5000。
2
20
40
输出有N行，分别对应输入的学生人数，每行输出剩下的学生最初的编号，编号之间有一个空格。
1 7 19
1 19 37
"""
from typing import Type
import threading

# n = input()
#
# for i in range(int(n)):
#     num = int(input())
#     while num > 3:
#         break


class A:
    def __init__(self):
        print("1111")


class B(A):
    def __init__(self):
        print('222')
        super().__init__()


class C(B):
    def __init__(self):
        super(B, self).__init__()

