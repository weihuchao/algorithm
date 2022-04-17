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
            x = 1 / float(x)

        ret = 1
        last_x = x

        """
        本题的核心点在于, n如果太大, 就会超时;
        为此需要将幂转化成加法, 刚好就是对n的二进制表示;
        二进制中1表示需要计算到结果, 0表示不需要计算到结果
        """
        while n > 0:
            n, d = divmod(n, 2)
            if d == 1:
                ret *= last_x
            last_x *= last_x
        return ret


def get_bin(n):
    r = []
    while n > 0:
        n, d = divmod(n, 2)
        r.append(str(d))

    return "".join(r)


if __name__ == '__main__':
    # print Solution().myPow(2.000, 10)
    # print Solution().myPow(0.00001, 2147483647)

    print get_bin(21)
    print bin(21)
    print get_bin(22)
    print bin(22)
"""
10101
0b10101

01101
0b10110
"""