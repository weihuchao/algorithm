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
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for idx in range(1, amount + 1):
            c = [sys.maxint]
            for coin in coins:
                if idx - coin < 0:
                    continue
                c.append(dp[idx - coin])
            dp[idx] = min(c) + 1
        return dp[amount] if dp[amount] < sys.maxint else -1


if __name__ == '__main__':
    # print Solution().coinChange([1, 2, 5], 11)
    print Solution().coinChange([2], 3)
    print Solution().coinChange([2], 4)
