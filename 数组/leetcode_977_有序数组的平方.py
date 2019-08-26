class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = []
        for i in range(len(A)):
            A[i] = abs(A[i])
        A.sort()
        for i in range(len(A)):
            m = A[i]*A[i]
            a.append(m)
        return a