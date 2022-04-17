#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        row, col = 0, n
        # while 0 <= row <= m and 0 <= col <= n:
        while row <= m and 0 <= col:
            print row, col
            val = matrix[row][col]
            if val == target:
                return True
            if val > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    print Solution().findNumberIn2DArray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)

    print Solution().findNumberIn2DArray([[-5]], -10)
