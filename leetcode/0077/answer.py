#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import copy


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self._combine(k, 1, n + 1 - (k - 1), [])
        return self.ret

    def _combine(self, k, start, end, ret):
        if len(ret) == k:
            return self.ret.append(ret)

        for val in range(start, end):
            c = copy.copy(ret)
            c.append(val)
            self._combine(k, val + 1, end + 1, c)


if __name__ == '__main__':
    print Solution().combine(4, 2)
