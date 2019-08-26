class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        length=len(T)
        res=[0 for i in range(length)]
        for i in range(length-2,-1,-1):
            j=i+1
            while j<length:
                if T[j]>T[i]:
                    res[i]=j-i
                    break
                elif res[j]==0:
                    res[i]=0
                    break
                j+=res[j]
        return res