#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        self.sums = []
        for idx in range(n):
            c, s = [0], 0
            for val in matrix[idx]:
                s += val
                c.append(s)
            self.sums.append(c)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        for row in range(row1, row2 + 1):
            ret += self.sums[row][col2 + 1] - self.sums[row][col1]
        return ret


if __name__ == '__main__':
    NM = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    for item in [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]:
        print NM.sumRegion(*item)
