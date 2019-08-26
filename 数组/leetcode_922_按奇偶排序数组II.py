class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = []
        b = []
        c = []
        for i in range(len(A)):
            if A[i] % 2 == 1:
                a.append(A[i])
            else:
                b.append(A[i])
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        return c