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
        ret = node = ListNode()
        q = []
        need_del = -1
        while head:
            if q:
                n = q.pop()
                if head.val == n.val:
                    need_del = head.val

                else:
                    need_del = -1
                    node.next = n
                    node = n
                    q.append(head)
            else:
                q.append(head)
            head = head.next
        # if q and q[0].val != need_del:


        return ret.next


if __name__ == '__main__':
    r = Solution().deleteDuplicates(
        ListNode(
            1,
            ListNode(
                2,
                ListNode(
                    3,
                    ListNode(
                        3,
                        ListNode(
                            4,
                            ListNode(
                                4,
                                ListNode(5, None)
                            )
                        )
                    )
                )
            )
        )
    )

    while r:
        print r.val
        r = r.next
