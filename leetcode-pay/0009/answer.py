#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao

class CQueue(object):

    def __init__(self):
        self._left_stack = []
        self._right_stack = []

    def _left_stack_empty(self):
        return len(self._left_stack) == 0

    def _left_stack_push(self, val):
        self._left_stack.append(val)

    def _left_stack_pop(self):
        val = self._left_stack[-1]
        self._left_stack = self._left_stack[:-1]
        return val

    def _right_stack_empty(self):
        return len(self._right_stack) == 0

    def _right_stack_push(self, val):
        self._right_stack.append(val)

    def _right_stack_pop(self):
        val = self._right_stack[-1]
        self._right_stack = self._right_stack[:-1]
        return val

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        while not self._right_stack_empty():
            self._left_stack_push(self._right_stack_pop())
        self._right_stack_push(value)
        while not self._left_stack_empty():
            self._right_stack_push(self._left_stack_pop())

    def deleteHead(self):
        """
        :rtype: int
        """
        if self._right_stack_empty():
            return -1
        return self._right_stack_pop()


if __name__ == '__main__':
    c = CQueue()
    c.appendTail(3)
    c.deleteHead()
    c.deleteHead()
    c.deleteHead()
