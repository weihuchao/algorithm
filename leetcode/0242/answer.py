#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sd = {}
        for k in s:
            sd.setdefault(k, 0)
            sd[k] += 1

        for k in t:
            if k not in sd:
                return False
            sd[k] -= 1

        return len([v for v in sd.values() if v != 0]) == 0
