class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = int(len(A)/2)
        for m in A:
            if A.count(m) == a:
                return m
