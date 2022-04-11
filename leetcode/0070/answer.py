#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        last, ret = 2, 3
        for _ in range(n - 3):
            last, ret = ret, last + ret
        return ret


if __name__ == '__main__':
    print Solution().climbStairs(1)
    print Solution().climbStairs(2)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
    print Solution().climbStairs(5)
