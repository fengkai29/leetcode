class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        a = []
        for i in range(num,-1,-1):
            b = []
            while i > 0:
                b.append(i % 2)
                i = int(i/2)
            a.append(b.count(1))
        a.reverse()
        return a


print(Solution().countBits(2))