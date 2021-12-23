#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.parent = {}
        self.travel(root)
        p_fathers = self.father_list(p)
        q_fathers = self.father_list(q)

        ret = None
        while p_fathers and q_fathers:
            if p_fathers[-1].val == q_fathers[-1].val:
                ret = p_fathers.pop()
                q_fathers.pop()
            else:
                return ret
        return ret

    def travel(self, root):
        if not root:
            return
        if root.left:
            self.parent[root.left.val] = root
            self.travel(root.left)
        if root.right:
            self.parent[root.right.val] = root
            self.travel(root.right)

    def father_list(self, root):
        if not root:
            return []
        ret = [root]
        while root.val in self.parent:
            root = self.parent[root.val]
            ret.append(root)
        return ret


if __name__ == '__main__':
    print Solution().lowestCommonAncestor(
        TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))),
        TreeNode(5),
        TreeNode(4)
    )
