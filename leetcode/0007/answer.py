#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        last = 1 if x > 0 else -1
        sv = list(str(abs(x)))
        sv.reverse()
        v = int("".join(sv)) * last
        if v > pow(2, 31) - 1 or v < -1 * pow(2, 31):
            return 0
        return v

if __name__ == '__main__':
    print Solution().reverse(1534236469)
    print Solution().reverse(-1563847412)
