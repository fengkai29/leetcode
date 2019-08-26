class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a = []
        for i in range(left,right+1):
            m = str(i)
            count = 0
            for j in range(len(m)):
                if int(m[j]) == 0:
                    break
                elif i%int(m[j])==0:
                    count = count + 1
            if count == len(m):
                a.append(i)
        return a