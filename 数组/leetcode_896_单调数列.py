class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==0 or len(A) == 1 or len(A) == 2:
            return True
        if A[len(A)-1]-A[0]>0:
            for i in range(len(A)-1):
                if A[i+1]<A[i]:
                    return False
                if i==len(A)-2:
                    return True
        if A[len(A)-1]-A[0]<0:
            for i in range(len(A)-1):
                if A[i+1]>A[i]:
                    return False
                if i==len(A)-2:
                    return True
        if A[len(A)-1]-A[0]==0:
            if A.count(A[0])==len(A):
                return True
            else:
                return False

a = [6,5,4,4]
print(Solution().isMonotonic(a))