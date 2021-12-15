#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
import sys


def get_mid_num(data):
    """
    解题思路: 单调栈
    首先拆解问题, 要求前面的数都比它小, 后面的数都比它大
    比它小很好解决, 只需要从前往后遍历, 查看是不是比当前最大值大就可以了
    后面的数都比它大, 这个需要借助单点(增)栈, 当后面出现小于栈内容的值的时候, 就应该出栈
    """
    ans = []
    maxn = -sys.maxint - 1
    for idx, val in enumerate(data):
        while len(ans) > 0 and val <= data[ans[-1]]:
            ans.pop()
        if val > maxn:
            maxn = val
            ans.append(idx)
    return ans


if __name__ == '__main__':
    print get_mid_num([3, 2, 1, 4, 7, 6, 5])
    print get_mid_num([2, 1, 3, 4, 5, 7, 6])
    print get_mid_num([7, 6, 5, 4, 3, 2, 1])
    print get_mid_num([6, 5, 4, 3, 2, 1, 7])
    print get_mid_num([1, 7, 6, 5, 4, 3, 2])
