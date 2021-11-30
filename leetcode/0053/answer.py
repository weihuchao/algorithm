#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = add_max = nums[0]
        for val in nums[1:]:
            add_max = max(val, add_max + val)
            ret = max(ret, add_max)
        return ret
