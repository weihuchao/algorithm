#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for idx, val in enumerate(height[1:]):
            for jdx in range(idx + 1):
                print idx, val, jdx
                ret = max(ret, min(val, height[jdx]) * (idx + 1 - jdx))
        return ret


if __name__ == '__main__':
    print Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
