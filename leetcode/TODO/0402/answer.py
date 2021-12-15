#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        num = [int(v) for v in num]
        for idx, val in enumerate(num):
            while k > 0 and stack and val < num[stack[-1]]:
                k -= 1
                stack.pop()
            stack.append(idx)
        for _ in range(k):
            stack.pop()

        ret = "".join([str(num[idx]) for idx in stack])
        ret = ret.lstrip("0")
        return ret if ret else "0"


if __name__ == '__main__':
    print Solution().removeKdigits("10", 2)
