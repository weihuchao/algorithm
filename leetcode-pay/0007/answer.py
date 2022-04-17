#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for a binary tree node.
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
        if not preorder:
            return
        root = TreeNode(preorder[0])
        self.preorder = preorder[1:]

        root_idx = inorder.index(root.val)
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]
        if left_inorder:
            root.left = self.buildTree(self.preorder, left_inorder)
        if right_inorder:
            root.right = self.buildTree(self.preorder, right_inorder)
        return root


if __name__ == '__main__':
    print Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
