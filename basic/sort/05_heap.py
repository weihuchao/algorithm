#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 22:13
# @Author  : weihuchao

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp


def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):  # 从最后一个非叶子结点开始建堆
        sift(data, i, n - 1)
    for i in range(n - 1, -1, -1):  # 这个i表示的是high
        data[0], data[i] = data[i], data[0]
        sift(data, 0, i - 1)
