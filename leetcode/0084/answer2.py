#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao
import sys


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        # 左边第一个比当前元素小的
        left_min = [-1 for _ in range(n)]
        stack = []
        for idx in range(n - 1, -1, -1):
            while len(stack) > 0 and heights[idx] < heights[stack[-1]]:
                s = stack.pop()
                left_min[s] = idx
            stack.append(idx)

        # 右边第一个比当前元素小的
        right_min = [n for _ in range(n)]
        stack = []
        for idx in range(n):
            while len(stack) > 0 and heights[idx] < heights[stack[-1]]:
                s = stack.pop()
                right_min[s] = idx
            stack.append(idx)

        return max([val * (right_min[idx] - left_min[idx] - 1) for idx, val in enumerate(heights)])


if __name__ == '__main__':
    print Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
    print Solution().largestRectangleArea([2, 1, 2])
