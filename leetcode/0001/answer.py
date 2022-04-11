#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        need_map = {}
        for idx, num in enumerate(nums):
            if num in need_map:
                return [idx, need_map[num]]
            else:
                need_map[target - num] = idx
        return []
