# -*- coding: utf-8 -*-
# Definition for a binary tree node.
"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
从前序与中序遍历序列构造二叉树
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        re = TreeNode(preorder[0])
        i = inorder.index(preorder[0])
        re.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        re.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return re


if __name__ == '__main__':
    s = Solution()
    pre = [3, 9, 20, 15, 7]
    inor = [9, 3, 15, 20, 7]
    print s.buildTree(pre, inor)
