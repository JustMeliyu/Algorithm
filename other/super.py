# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-28
Describe:
super 用法
"""


class A:
    def __init__(self):
        print("1111")


class B(A):
    def __init__(self):
        print('222')
        super().__init__()


class C(B):
    def __init__(self):
        super().__init__()


class D(B):
    def __init__(self):
        super(D, self).__init__()


class E(B):
    def __init__(self):
        super(B, self).__init__()


if __name__ == '__main__':
    c = C()
    d = D()
    e = E()
