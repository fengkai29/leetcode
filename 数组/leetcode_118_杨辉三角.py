class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        a = [[1],[1,1]]
        for i in range(2,numRows):
            b = []
            b.append(1)
            for j in range(1,len(a[i-1])):
                b.append(a[i-1][j]+a[i-1][j-1])
            b.append(1)
            a.append(b)
        return a

print(Solution().generate(5))