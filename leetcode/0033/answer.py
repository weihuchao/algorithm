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
            if nums[mid] == target:
                return mid
            if nums[0] < nums[mid - 1]:
                if nums[0] <= target <= nums[mid - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[len(nums) - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    print Solution().search([1], 0)
