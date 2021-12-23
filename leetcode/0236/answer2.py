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

        self.visted = {p.val: True}
        while p.val in self.parent:
            p = self.parent[p.val]
            self.visted[p.val] = True

        while q:
            if q.val in self.visted:
                return q
            else:
                q = self.parent[q.val]
        return

    def travel(self, root):
        if not root:
            return
        if root.left:
            self.parent[root.left.val] = root
            self.travel(root.left)
        if root.right:
            self.parent[root.right.val] = root
            self.travel(root.right)


if __name__ == '__main__':
    print Solution().lowestCommonAncestor(
        TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))),
        TreeNode(5),
        TreeNode(4)
    )
