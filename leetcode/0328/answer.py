#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first, second = ListNode(0, head), ListNode()
        f, s = first, second
        idx = 0
        while head.next:
            if idx % 2 == 0:
                first.next, head = head, head.next
                first = first.next
            else:
                second.next, head = head, head.next
                second = second.next
            idx += 1
        first.next = s.next
        return f

