#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/6 12:17
# @Author  : weihuchao
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix[0])
        for row_idx in range(1, n):
            for col_idx, val in enumerate(matrix[row_idx]):
                c = [matrix[row_idx - 1][col_idx]]
                if 0 <= col_idx - 1:
                    c.append(matrix[row_idx - 1][col_idx - 1])
                if col_idx + 1 < n:
                    c.append(matrix[row_idx - 1][col_idx + 1])
                matrix[row_idx][col_idx] = val + min(c)
        return min(matrix[-1])


if __name__ == '__main__':
    print Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    print Solution().minFallingPathSum([[-19, 57], [-40, -5]])
    print Solution().minFallingPathSum([[-48]])
