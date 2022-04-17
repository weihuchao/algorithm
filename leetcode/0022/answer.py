#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cache = {
            1: {"()"},
            2: {"()()", "(())"},
        }
        for i in range(n - 2):
            current = set()
            for mid in cache[i + 3 - 1]:
                current.add("(" + mid + ")")
            for j in range(1, i + 3):
                for left in cache[j]:
                    for right in cache[i + 3 - j]:
                        current.add(left + right)
            cache[i + 3] = current
        return list(cache[n]) if n in cache else []


if __name__ == '__main__':
    print Solution().generateParenthesis(1)
    print Solution().generateParenthesis(2)
    print Solution().generateParenthesis(3)
    print Solution().generateParenthesis(4)
