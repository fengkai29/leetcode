class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = []
        while n != 1:
            if n in a:
                return False
            a.append(n)
            n = self.func(n)
        return True

    def func(self,m):
        ans = 0
        while m != 0:
            a = m % 10
            m = int(m / 10)
            ans = ans + a**2
        return ans

