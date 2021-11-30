#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, h = 0, 1
        for _ in range(n):
            p, h = h, p + h
        return p


if __name__ == '__main__':
    print Solution().fib(2)
