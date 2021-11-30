#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 21:04
# @Author  : weihuchao
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_val, num2_val = 0, 0
        for idx, c in enumerate(num1):
            num1_val += 10 ** (len(num1) - idx - 1) * int(c)
        for idx, c in enumerate(num2):
            num2_val += 10 ** (len(num2) - idx - 1) * int(c)
        return str(num1_val + num2_val)
