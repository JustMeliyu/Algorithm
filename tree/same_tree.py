# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-27"

"""
Describe: 校验两个二叉数是否相同, 即结构以及值是否均相同
"""
from tools.construction import TreeNode


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if q is None and p is None:
            return True
        elif (q is None and p is not None) or (q is not None and p is None):
            return False
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def is_same_tree2(self, p: TreeNode, q: TreeNode) -> bool:
        if q is not None and p is not None:
            return p.val == q.val and self.is_same_tree2(p.left, q.left) and self.is_same_tree2(p.right, q.right)
        return q == p


if __name__ == '__main__':
    tree1 = TreeNode("a", TreeNode("b", TreeNode("d"), TreeNode("e")), TreeNode("c"))
    tree2 = TreeNode("a", TreeNode("b", TreeNode("d"), TreeNode("e")), TreeNode("c"))

    s = Solution()
    print(s.is_same_tree2(tree1, tree2))
