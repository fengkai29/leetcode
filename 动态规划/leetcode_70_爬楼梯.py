# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n>2:
#             return self.climbStairs(n-1)+self.climbStairs(n-2)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        a1 = 1
        a2 = 2
        a3 = 0
        while(n > 2):
            a3 = a1 + a2
            a1 = a2
            a2 = a3
            a3 = 0
            n -= 1
        return a2


n = 28
print(Solution().climbStairs(n))