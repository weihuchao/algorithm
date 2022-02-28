#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queque = [root]
        second_queque = []
        ret = []
        while queque:
            last_val = None
            for node in queque:
                if node.left:
                    second_queque.append(node.left)
                if node.right:
                    second_queque.append(node.right)
                last_val = node.val
            ret.append(last_val)
            queque = second_queque
            second_queque = []
        return ret
