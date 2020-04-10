# -*- coding: utf-8 -*-
"""
__author__ = "Road36"
__date__ = "19-12-26"
Describe:
路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
示例: 
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""

from tools.construction import TreeNode


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int, 和
        :rtype: bool
        """
        # if not root:
        #     # if sum == 0:
        #     #     return True
        #     return False
        # # if sum < 0:
        # #     return False
        # sum -= root.val
        # if root.left is None and root.right is None:
        #     return sum == 0
        # return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == '__main__':
    r = TreeNode(5, TreeNode(4, TreeNode(11, 7, 2)), TreeNode(8, TreeNode(13), TreeNode(4, None, 1)))
    _sum = 22
    s = Solution()
    s.hasPathSum(r, _sum)
