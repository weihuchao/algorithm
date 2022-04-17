#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1 / x

        ret, last_x = 1, x
        while n > 0:
            n, d = divmod(n, 2)
            if d == 1:
                ret *= last_x
            last_x *= last_x
        return ret


if __name__ == '__main__':
    print Solution().myPow(2.000, 10)
    print Solution().myPow(0.00001, 2147483647)
