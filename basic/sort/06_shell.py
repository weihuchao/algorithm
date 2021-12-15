#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/15 22:28
# @Author  : weihuchao
def shell_sort(li):
    gap = len(li) // 2
    while gap > 0:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap /= 2
