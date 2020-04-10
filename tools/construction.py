# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-10
Describe:
数据结构
"""


class TreeNode:
    """二叉树"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ChainNode:
    """链表"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
