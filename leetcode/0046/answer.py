#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ret = [[nums[0]]]
        for val in nums[1:]:
            current = []
            for item in ret:
                for idx in range(len(ret[0]) + 1):
                    data = copy.copy(item)
                    data.insert(idx, val)
                    current.append(data)
            ret = current
        return ret


if __name__ == '__main__':
    print Solution().permute([1, 2, 3])
