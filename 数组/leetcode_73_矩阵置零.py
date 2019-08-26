class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a = []
        b = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    a.append(i)
                    b.append(j)
        a = set(a)
        b = set(b)
        for i in a:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in b:
            for j in range(len(matrix)):
                matrix[j][i] = 0

