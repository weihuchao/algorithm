#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 22:00
# @Author  : weihuchao

def insert_sort(data):
    """
    从前往后遍历, 假定前面部分已经有序, 查看当前元素应该在前面部分的哪个位置
    """
    for idx in range(1, len(data)):
        tmp = data[idx]
        j = idx - 1
        while j >= 0 and tmp < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = tmp
