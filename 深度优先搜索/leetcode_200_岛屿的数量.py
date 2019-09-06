class Solution(object):
    def __init__(self):
        self.dec = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        mark = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(m):
            for j in range(n):
                if (not mark[i][j]) and grid[i][j] == '1':
                    count = count + 1
                    self.dfs(grid, i, j, m, n, mark)
        return count

    def dfs(self, grid, i, j, m, n, mark):
        mark[i][j] = True
        for dec in self.dec:
            new_i = i + dec[0]
            new_j = j + dec[1]
            if 0 <= new_i < m and 0 <= new_j < n:
                if (not mark[new_i][new_j]) and grid[new_i][new_j] == '1':
                    self.dfs(grid, new_i, new_j, m, n, mark)

if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result)



