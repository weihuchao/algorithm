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
        if not head or not head.next:
            return head
        head_next = head.next
        head.next = self.swapPairs(head_next.next)
        head_next.next = head
        return head_next


if __name__ == '__main__':
    # Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
