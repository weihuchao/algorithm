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

        m, n = len(matrix), len(matrix[0])

        def row_bin_search(row_start, row_end, col):
            while row_start < row_end:
                mid = (row_start + row_end) / 2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] > target:
                    row_end = mid
                else:
                    row_start = mid + 1

            return row_start

        def col_bin_search(col_start, col_end, row):
            while col_start < col_end:
                mid = (col_start + col_end) / 2
                if matrix[row][mid] == target:
                    return True, -1
                elif matrix[row][mid] > target:
                    col_end = mid
                else:
                    col_start = mid + 1
            return False, col_start

        # 思路是: 在行和列中不断二分, 但是实现起来非常困难
        sr, er, sc, ec = 0, m - 1, 0, n - 1
        for _ in range(30):
            find, row = row_bin_search(sr, er, sc)
            print find, row
            if find:
                return True

            find, col = col_bin_search(sc, ec, row - 1)
            print find, row
            if find:
                return True
        return False


if __name__ == '__main__':
    print Solution().findNumberIn2DArray([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)

    # print Solution().findNumberIn2DArray([[-5]], -10)
