#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao
import sys


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        ret = matrix[0][0]
        idx_list = [0 for _ in range(n)]
        for _ in range(k):
            c = []
            for idx in range(n):
                if idx_list[idx] < n:
                    c.append(matrix[idx][idx_list[idx]])
                else:
                    c.append(sys.maxint)
            ret = min(c)
            idx_list[c.index(ret)] += 1
        return ret
