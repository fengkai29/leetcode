class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 1:
            return triangle[0][0]
        triangle[1][0] = triangle[1][0] + triangle[0][0]
        triangle[1][1] = triangle[1][1] + triangle[0][0]
        for i in range(2,len(triangle)):
            for j in range(1,i):
                triangle[i][j] = triangle[i][j]+min(triangle[i-1][j-1],triangle[i-1][j])
            triangle[i][0] = triangle[i][0] + triangle[i-1][0]
            triangle[i][len(triangle[i])-1] = triangle[i][len(triangle[i])-1] + triangle[i-1][len(triangle[i-1])-1]
        return min(triangle[len(triangle)-1])