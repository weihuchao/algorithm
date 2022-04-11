#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, last_idx, last_map = 0, -1, {}
        for idx, c in enumerate(s):
            if c in last_map and last_map[c] > last_idx:
                last_idx = last_map[c]
            last_map[c] = idx
            ret = max(ret, idx - last_idx)
        return ret


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abc")
    print Solution().lengthOfLongestSubstring("abca")
    print Solution().lengthOfLongestSubstring("abcbcad")
