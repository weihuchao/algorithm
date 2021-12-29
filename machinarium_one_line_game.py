#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 11:24
# @Author  : weihuchao
import copy
import json


def dfs(z, m, n, data, path, last_point, count, d=None):
    z.append(0)
    i, j = last_point
    if d in [0, 3]:
        next_i_list = range(i - 1, -1, -1) if d == 0 else range(i + 1, m)
        for next_i in next_i_list:
            if data[next_i][j] == 0:
                data[next_i][j] = 1
                count += 1
                last_point = (next_i, j)
            else:
                break
    if d in [1, 2]:
        next_j_list = range(j - 1, -1, -1) if d == 1 else range(j + 1, n)
        for next_j in next_j_list:
            if data[i][next_j] == 0:
                data[i][next_j] = 1
                count += 1
                last_point = (i, next_j)
            else:
                break
    if count == m * n:
        print json.dumps(path, ensure_ascii=False, encoding="utf8")
        return

    i, j = last_point
    ds = []
    if -1 < i - 1 < 5 and data[i - 1][j] == 0:
        ds.append(0)
    if -1 < j - 1 < 5 and data[i][j - 1] == 0:
        ds.append(1)
    if -1 < j + 1 < 5 and data[i][j + 1] == 0:
        ds.append(2)
    if -1 < i + 1 < 5 and data[i + 1][j] == 0:
        ds.append(3)
    d_map = {0: u"上", 1: u"左", 2: u"右", 3: u"下"}
    for d in ds:
        c = copy.deepcopy(data)
        p = copy.deepcopy(path)
        p.append(d_map[d])
        dfs(z, m, n, c, p, last_point, count, d)


def get_one_line(m=5, n=5, stone=None):
    data = [[0 for _ in range(m)] for _ in range(n)]
    if stone is not None:
        for i, j in stone:
            data[i][j] = 1
    count = len(stone) + 1 if stone else 1

    z = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == 0:
                r = copy.deepcopy(data)
                r[i][j] = 1
                dfs(z, m, n, r, [(i, j), ], (i, j), count)

    print len(z)


if __name__ == '__main__':
    get_one_line(5, 5, [(0, 4), (2, 3), (3, 0), (4, 2)])
