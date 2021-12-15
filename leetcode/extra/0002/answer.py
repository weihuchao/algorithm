#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao


def f(n, m, l, k):
    if m == 0:
        print ' '.join(l)
    for i in range(k, n + 1):
        if i > m:
            break
        l.append(str(i))
        f(n, m - i, l, i + 1)
        l.pop()


if __name__ == '__main__':
    f(10, 7, [], 1)
