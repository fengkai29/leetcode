class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = []
        for i in range(len(A[0])):
            a = []
            for j in range(len(A)):
                a.append(A[j][i])
            m.append(a)
        return m