#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s, e = 0, num
        while s <= e:
            mid = (s + e) / 2
            print s, e, mid
            v = mid * mid
            if v == num:
                return True
            elif v < num:
                s = mid + 1
            else:
                e = mid - 1
        return False


if __name__ == '__main__':
    print Solution().isPerfectSquare(16)
