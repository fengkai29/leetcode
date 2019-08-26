class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            for j in range(int(len(A[i])/2)):
                temp = A[i][j]
                A[i][j] = A[i][len(A[i])-j-1]
                A[i][len(A[i])-j-1] = temp
        for k in range(len(A)):
            for l in range(len(A[i])):
                if A[k][l] == 0:
                    A[k][l] = 1
                else :
                    A[k][l] = 0
        return A


m  = [[1,1,0],[1,0,1],[0,0,0]]
t = Solution().flipAndInvertImage(m)
print(t)