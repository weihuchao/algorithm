#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def dfs(cur):
            if not cur:
                return

            dfs(cur.left)

            if self.pre:
                # 将前一个node和当前node建立双指针
                self.pre.right, cur.left = cur, self.pre
            else:
                # 找到头部
                self.head = cur
            # 前一个node切换到当前node
            self.pre = cur

            dfs(cur.right)

        if not root:
            return
        self.pre, self.head = None, None
        dfs(root)
        # 此时self.pre是最后一个node, 它的left已经设置好了, 只需要再和self.head建立连接就可以了
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
