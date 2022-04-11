#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import sys


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        ret = []
        while amount >= 0:
            pass

        def getChange(c, a):
            if a == 0:
                return True
            ret.append(c[0])
            getChange(c[1:], a)


if __name__ == '__main__':
    print Solution().coinChange([1, 2, 5], 11)
    # print Solution().coinChange([2], 3)
    # print Solution().coinChange([2], 4)
