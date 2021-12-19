#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = pre = ListNode()
        while head:
            pre, head = self.exchange(pre, head)
        return node.next

    def exchange(self, pre, head):
        n = None
        if head.next:
            node = head.next
            head.next = None
            n = node.next
            node.next = head
            pre.next = node
        else:
            pre.next = head
        return head, n


if __name__ == '__main__':
    # Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
