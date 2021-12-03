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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret, queue = [], [root]
        while queue:
            c = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                c.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(c)

        for idx, val in enumerate(ret):
            if idx % 2 == 1:
                val.reverse()
        return ret
