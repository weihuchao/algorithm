#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_v = 0
        for idx, v in enumerate(heights):
            max_v = max(max_v, v)
            current_low = v
            for jdx in range(idx + 1, len(heights)):
                if heights[jdx] < current_low:
                    current_low = heights[jdx]
                max_v = max(max_v, current_low * (jdx - idx + 1))
        return max_v
