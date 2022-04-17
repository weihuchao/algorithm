#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class MyQueue(object):

    def __init__(self):
        self._data = []
        self._size = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._data.append(x)
        self._size += 1

    def pop(self):
        """
        :rtype: int
        """
        v = self._data[0]
        self._data = self._data[1:]
        self._size -= 1
        return v

    def peek(self):
        """
        :rtype: int
        """
        return self._data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self._size == 0


if __name__ == '__main__':
    q = MyQueue()
    print q.push(1)
    print q.push(2)
    print q.peek()
    print q.pop()
    print q.empty()
