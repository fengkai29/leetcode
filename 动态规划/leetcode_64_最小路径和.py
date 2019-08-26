class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(grid)):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                if grid[i-1][j]>=grid[i][j-1]:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                else:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
        return grid[len(grid)-1][len(grid[0])-1]