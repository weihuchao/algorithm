#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        current_target = sum(nums[:3])
        for idx, val in enumerate(nums):
            start = idx + 1
            end = nums_len - 1
            while start < end < nums_len:
                sum_val = val + nums[start] + nums[end]
                if sum_val == target:
                    return target
                if abs(target - sum_val) < abs(target - current_target):
                    current_target = sum_val
                if sum_val > target:
                    end -= 1
                else:
                    start += 1
        return current_target


if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print Solution().threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82)
