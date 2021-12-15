#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/4 22:03
# @Author  : weihuchao

def partition(data, left, right):
    pivot = data[left]
    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        data[left] = data[right]
        # left += 1

        while left < right and data[left] <= pivot:
            left += 1
        data[right] = data[left]
        # right -= 1
    data[left] = pivot
    return left


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)
