#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for idx in range(m + 1):
            dp[idx][0] = idx
        for idx in range(n + 1):
            dp[0][idx] = idx

        for idx in range(1, m + 1):
            for jdx in range(1, n + 1):
                if word1[idx - 1] == word2[jdx - 1]:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1]
                else:
                    dp[idx][jdx] = min(dp[idx - 1][jdx - 1], dp[idx][jdx - 1], dp[idx - 1][jdx]) + 1

        return dp[m][n]


if __name__ == '__main__':
    print Solution().minDistance("horse", "ros")
