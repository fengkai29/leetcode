class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 9
        temp = 10
        if n == 0:
            return 1
        if n == 1:
            return 10
        else:
            for i in range(1,n):
                ans = ans *(10-i)
                m = ans + temp
                temp = ans

        return m