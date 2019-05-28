# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-28"

"""
Describe:
BST: Binary Search Tree
验证是否为二叉搜索树,
    1.左节点小于根节点
    2.右节点大于根节点
    3.左子树右字数包含以上特点
"""
from DFS.tree import Tree


class Solution:
    def isValidBST(self, root: Tree) -> bool:
        if root.left:
            if root.val < root.left:
                return False
            self.isValidBST(root.left)
        if root.right:
            if root.val > root.right:
                return False
            self.isValidBST(root.right)
