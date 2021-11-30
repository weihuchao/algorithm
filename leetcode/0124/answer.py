#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = root.val
        self.get_child_max(root)
        return self.ret

    def get_child_max(self, node):
        if not node:
            return 0
        left_max = self.get_child_max(node.left)
        right_max = self.get_child_max(node.right)
        child_max = max(node.val, node.val + left_max, node.val + right_max)
        self.ret = max(self.ret, child_max, node.val + left_max + right_max)
        return child_max
