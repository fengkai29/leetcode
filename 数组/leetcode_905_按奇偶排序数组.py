class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        c = []
        for i in range(len(A)):
            if A[i]%2 == 1:
                a.append(A[i])
            else:
                b.append(A[i])
        c = b + a
        return c