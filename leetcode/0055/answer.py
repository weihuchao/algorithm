#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_idx = 0
        for idx in range(len(nums)):
            if idx <= max_idx:
                max_idx = max(max_idx, nums[idx] + idx)
            if max_idx >= len(nums) - 1:
                return True
        return False


if __name__ == '__main__':
    print Solution().canJump([2, 0, 0, 1, 3, 2])
