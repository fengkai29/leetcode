class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mi = min(A)
        ma = max(A)
        if ma-mi-2*K<=0:
            return 0
        else:
            return ma-mi-2*K