#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 21:56
# @Author  : weihuchao

def select_sort(data):
    """
    从前往后遍历, 包括当前元素在内后面的所有的元素, 找到最小的值, 放到当前位置
    """
    for idx in range(len(data) - 1):
        min_loc = idx
        for j in range(idx + 1, len(data)):
            if data[j] < data[min_loc]:
                min_loc = j
        if min_loc != idx:
            data[idx], data[min_loc] = data[min_loc], data[idx]
