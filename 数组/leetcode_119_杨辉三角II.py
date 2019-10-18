class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [[1],[1,1]]
        if rowIndex == 0 or rowIndex == 1:
            return res[rowIndex]
        for i in range(2,rowIndex+1):
            ls = []
            ls.append(1)
            for j in range(len(res[i-1])-1):
                ls.append(res[i-1][j]+res[i-1][j+1])
            ls.append(1)
            res.append(ls)
        return res[-1]