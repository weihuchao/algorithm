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
        ans, add = [], 0
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or add > 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            add, r = divmod(x + y + add, 10)
            ans.append(str(r))
            i -= 1
            j -= 1
        ans.reverse()
        return "".join(ans)


if __name__ == '__main__':
    print Solution().addStrings("124", "11")
    print Solution().addStrings("456", "77")
