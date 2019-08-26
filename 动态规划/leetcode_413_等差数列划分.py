class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        count = 2
        i = 1
        while i < len(A)-1:
            if A[i] - A[i-1] == A[i+1] - A[i]:
                count = count + 1
                i = i + 1
            else:
                if count >=3:
                    ans = ans + ((count-1)*(count-2))/2
                count = 2
                i = i + 1
        if count>=3:
            ans = ans = ans + ((count-1)*(count-2))/2
        return ans
