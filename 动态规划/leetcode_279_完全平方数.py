# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 1
#         flag = 0
#         i = 1
#         j = 1
#         a = []
#         b = []
#         while i * i <= n:
#             a.append(n - i * i)
#             i += 1
#         while flag not in a and flag not in b:
#             for i in range(len(a)):
#                 while j * j<=a[i]:
#                     b.append(a[i]-j*j)
#                     j += 1
#                 j = 1
#             a = []
#             count = count + 1
#             if flag in b:
#                 return count
#             for i in range(len(b)):
#                 while j * j<=b[i]:
#                     a.append(b[i]-j*j)
#                     j += 1
#                 j = 1
#             b = []
#             count = count + 1
#             if flag in a:
#                 return count
#         return count

class Solution:
    def numSquares(self, n):
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[-j*j] for j in range(1, 1 + int(i**0.5))) + 1)
        return dp[-1]



print(Solution().numSquares(6255))
