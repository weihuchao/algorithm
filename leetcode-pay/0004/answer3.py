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
            while row_start <= row_end:
                mid = (row_start + row_end) / 2
                if matrix[mid][col] == target:
                    return True
                elif matrix[mid][col] > target:
                    row_end = mid - 1
                else:
                    row_start = mid + 1
            return False

        def col_bin_search(col_start, col_end, row):
            while col_start <= col_end:
                mid = (col_start + col_end) / 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    col_end = mid - 1
                else:
                    col_start = mid + 1
            return False

        if m == 0:
            return col_bin_search(0, n, 0)
        if n == 0:
            return row_bin_search(0, m, 0)

        # 先定位右下角
        row, col = 0, 0
        while matrix[row][col] <= target:
            if matrix[row][col] == target:
                return True
            row = (row + 1) % m
            col = (col + 1) % n
            if row == col == 0:
                break

        if row_bin_search(0, row, col):
            return True
        return col_bin_search(0, col, row)


if __name__ == '__main__':
    # print Solution().findNumberIn2DArray([
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ], 5)

    # print Solution().findNumberIn2DArray([[-5]], -10)
    # print Solution().findNumberIn2DArray([[-5]], -2)
    # print Solution().findNumberIn2DArray([[-5]], -5)

    print Solution().findNumberIn2DArray([[1, 4], [2, 5]], 2)

    # print Solution().findNumberIn2DArray([
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ], 20)
