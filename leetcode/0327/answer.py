#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        idx_list, val_list = [], []
        for idx, val in enumerate(nums):
            if lower <= val <= upper:
                idx_list.append(idx)
                val_list.append(val)
        for i in range(len(idx_list) - 1):
            for j in range(i + 1, len(idx_list)):
                val_list.append(sum(nums[idx_list[i]:idx_list[j] + 1]))
        return len(set(val_list))


if __name__ == '__main__':
    print Solution().countRangeSum([-2, 5, -1], -2, 2)
