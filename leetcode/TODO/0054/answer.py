class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        (0, 0) (0, 4) (4, 4) (4, 0)
        (1, 0) (1, 3) (3, 3)
        
        
        0-0 0-2 2-2 2-0 (i, j, k, l = 0, 0, 2, 2)
        1-0 1-1
        
        0-0 0-3 2-3 2-0
        1-0 1-2 1-2
        """
