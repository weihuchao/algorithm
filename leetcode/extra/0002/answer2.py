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
        for i in range(1, n + 1):
            self._get_combine(i + 1, n, k - i, [i])
        return self.ret

    def _get_combine(self, start, end, target, arr):
        if target == 0:
            self.ret.append(arr)
            return
        for i in range(start, end + 1):
            if i > target:
                break
            c = copy.copy(arr)
            c.append(i)
            self._get_combine(i + 1, end, target - i, c)


if __name__ == '__main__':
    print Solution().combine(10, 7)
    print Solution().combine(15, 9)
