#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s, t, ret = 0, x, -1
        while s <= t:
            mid = (s + t) / 2
            if mid * mid <= x:
                ret = mid
                s = mid + 1
            else:
                t = mid - 1
        return ret
