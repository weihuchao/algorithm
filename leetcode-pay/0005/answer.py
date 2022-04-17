#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = []
        for c in s:
            if c == " ":
                r.append("%20")
            else:
                r.append(c)
        return "".join(r)
