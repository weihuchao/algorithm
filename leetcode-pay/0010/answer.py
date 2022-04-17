#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre, ret = 0, 1
        if n < 2:
            return n

        while n > 1:
            n -= 1
            pre, ret = ret, (pre + ret) % 1000000007
        return ret
