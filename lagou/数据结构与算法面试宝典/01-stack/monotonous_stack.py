#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 18:42
# @Author  : weihuchao

def run_problem1(data):
    """
    【题目】一个整数数组 A，找到每个元素：右边第一个比我小的下标位置，没有则用 -1 表示。
    输入：[5, 2]
    输出：[1, -1]
    """
    ret = [-1 for _ in range(len(data))]
    stack = []
    for idx, v in enumerate(data):
        while len(stack) > 0 and v < data[stack[-1]]:
            s = stack.pop()
            ret[s] = idx
        stack.append(idx)
    return ret


def run_problem2(data, k):
    """
    【题目】给定一个正整数数组和 k，要求依次取出 k 个数，输出其中数组的一个子序列，需要满足：1. 长度为 k；2.字典序最小。
    输入：nums = [3,5,2,6], k = 2
    输出：[2,6]
    """
    stack = []
    total = len(data)
    for idx, v in enumerate(data):
        while len(stack) > 0 and len(stack) + total - idx > k and v < stack[-1]:
            stack.pop()
        stack.append(v)

    while len(stack) > k:
        stack.pop()
    return stack


def run_problem3(data):
    """
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
    【题目】给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为1。求在该柱状图中，能够勾勒出来的矩形的最大面积。
    输入：heights = [2,1,5,6,2,3]
    输出：10
    """
    max_v = 0
    for idx, v in enumerate(data):
        max_v = max(max_v, v)
        current_low = v
        for jdx in range(idx + 1, len(data)):
            if data[jdx] < current_low:
                current_low = data[jdx]
            max_v = max(max_v, current_low * (jdx - idx + 1))
    return max_v


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


if __name__ == '__main__':
    # print run_problem1([1, 2, 4, 9, 4, 0, 5])
    # print run_problem2([9, 2, 4, 5, 1, 2, 3, 0], 3)

    print run_problem3([2, 1, 5, 6, 2, 3])
    print run_problem3([2, 4])
