#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        r = []
        while head:
            r.append(head.val)
            head = head.next
        r.reverse()
        return r


if __name__ == '__main__':
    print Solution().reversePrint(ListNode(1, ListNode(2, ListNode(3, None))))
