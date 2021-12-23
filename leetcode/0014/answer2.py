#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        max_n = min([len(s) for s in strs])
        ret = strs[0][:max_n]

        for s in strs[1:]:
            n = len(ret)
            for idx, val in enumerate(s):
                if idx >= n or ret[idx] != val:
                    ret = ret[:idx]
                    break
        return ret


if __name__ == '__main__':
    print Solution().longestCommonPrefix(["flower", "flow", "flight"])
