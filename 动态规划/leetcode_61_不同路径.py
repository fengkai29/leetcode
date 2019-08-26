class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # if m > 1 and n > 1:
        #     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        # elif n == 1 and m != 1:
        #     return 1
        # elif m == 1 and n != 1:
        #     return 1
        # else:
        #     return 0
        a =[]
        for i in range(m):
            a.append([])
            for j in range(n):
                a[i].append(0)
        for i in range(m):
            a[i][0] = 1
        for i in range(n):
            a[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                a[i][j] = a[i-1][j] + a[i][j-1]
        return a[m-1][n-1]


a = 3
b = 2
print(Solution().uniquePaths(a,b))