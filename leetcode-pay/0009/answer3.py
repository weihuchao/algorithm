# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import collections


class CQueue(object):

    def __init__(self):
        self.left = collections.deque()
        self.right = collections.deque()

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.left.append(value)

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.right:
            return self.right.pop()
        else:
            while self.left:
                self.right.append(self.left.pop())
            return self.right.pop() if self.right else -1


if __name__ == '__main__':
    c = CQueue()
    c.appendTail(1)
    c.appendTail(3)
    print c.deleteHead()
    print c.deleteHead()
    print c.deleteHead()
    c.appendTail(4)
    print c.deleteHead()
    print c.deleteHead()
