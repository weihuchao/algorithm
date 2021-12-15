#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 21:50
# @Author  : weihuchao

def bubble_sort(data):
    """
    从前往后冒泡, 每次在后面完成一个就位的元素
    """
    data_len = len(data)
    for idx in range(data_len - 1):
        for j in range(data_len - idx - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def bubble_sort2(data):
    """
    记录下本轮交换的情况, 如果没有交换, 说明序列已经有序
    """
    idx = len(data) - 1
    while idx > 0:
        last_idx = 0
        for j in range(idx):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                last_idx = j
        idx = 0 if last_idx == 0 else last_idx
    return data
