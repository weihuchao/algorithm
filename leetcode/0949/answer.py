#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        arr.sort()
        ret_val, ret_str = -1, ""

        def get_time(a, b, c, d):
            hour, min = a * 10 + b, c * 10 + d
            if hour > 23:
                return False, 0
            if min > 59:
                return False, 0
            return True, hour * 100 + min

        for a in range(4):
            for b in range(4):
                if b == a:
                    continue
                for c in range(4):
                    if c in [a, b]:
                        continue
                    for d in range(4):
                        if d in [a, b, c]:
                            continue
                        z, v = get_time(arr[a], arr[b], arr[c], arr[d])
                        if z and v > ret_val:
                            ret_str = "%s%s:%s%s" % (arr[a], arr[b], arr[c], arr[d])
        return ret_str
