#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = {}
        for val in nums:
            counts.setdefault(val, 0)
            counts[val] += 1
        return [val for val, count in counts.items() if count == 1]
