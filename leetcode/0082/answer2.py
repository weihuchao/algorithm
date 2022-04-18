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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ret = node = ListNode(1, head)

        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                x = node.next.val
                while node.next and node.next.val == x:
                    node.next = node.next.next
            else:
                node = node.next
        return ret.next


if __name__ == '__main__':
    r = Solution().deleteDuplicates(
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None))))))))

    while r:
        print r.val
        r = r.next
