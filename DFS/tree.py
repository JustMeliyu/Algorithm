# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-28"

"""
Describe:
初始化树结构
"""


class Tree:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
