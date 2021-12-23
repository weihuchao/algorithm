#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for val in nums:
            v = int(val)
            if 1 <= v <= len(nums):
                nums[v - 1] = unicode(nums[v - 1])
        for idx, val in enumerate(nums, 1):
            if not isinstance(val, unicode):
                return idx
        return len(nums) + 1


if __name__ == '__main__':
    print Solution().firstMissingPositive([1, 2, 0])
    print Solution().firstMissingPositive([3, 4, -1, 1])
    print Solution().firstMissingPositive([7, 8, 9, 11, 12])
    print Solution().firstMissingPositive([2, 1])
    print Solution().firstMissingPositive([1])
