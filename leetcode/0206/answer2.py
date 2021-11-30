#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, node = None, head
        while node:
            pre, node = self.reverse(pre, node)
        return pre

    def reverse(self, pre, node):
        next = node.next
        node.next = pre
        return node, next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    p = Solution().reverseList(head)
    print p.val
