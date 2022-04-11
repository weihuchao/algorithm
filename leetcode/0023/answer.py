#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
# Definition for singly-linked list.
import sys


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [n for n in lists if n]
        if not lists:
            return
        head = node = ListNode()
        while len(lists) > 0:
            min_val, min_idx = sys.maxint, 0
            for idx, n in enumerate(lists):
                if n.val < min_val:
                    min_val = n.val
                    min_idx = idx
            node.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            node = node.next
            lists = [n for n in lists if n]
        return head.next