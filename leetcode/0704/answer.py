#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            n = nums[mid]
            if target < n:
                end = mid - 1
            elif target == n:
                return mid
            else:
                start = mid + 1
        return -1
