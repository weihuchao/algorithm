#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return True
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


if __name__ == '__main__':
    print Solution().search([1, 0, 1, 1, 1], 0)
