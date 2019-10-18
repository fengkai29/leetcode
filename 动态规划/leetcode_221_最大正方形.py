class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        if '1' in matrix[0]:
            res = 1
        for i in range(row):
            if '1' == matrix[i][0]:
                res = 1
                break
        dp = [[0]*col for _ in range(row)]
        for i in range(1,col):
            for j in range(1,row):
                if matrix[j][i] == '1':
                    matrix[j][i] = min(int(matrix[j-1][i]),int(matrix[j-1][i-1]),int(matrix[j][i-1]))+1
                    res = max(res,matrix[j][i]**2)

        return res
m = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]

print(Solution().maximalSquare(m))
