# class Solution(object):
#     def findUnsortedSubarray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         for i in range(len(nums)):
#             if nums[i]>min(nums[i:len(nums)]):
#                 break
#             else:
#                 n = n-1
#         for i in range(len(nums)-1,1,-1):
#             if nums[i]<max(nums[0:i]):
#                 break
#             else:
#                 n=n-1
#         if n<0:
#             return 0
#         return n

class Solution(object):
    def findUnsortedSubarray(self, nums):
        k = sorted(nums)
        p1 = 0
        p2 = len(nums)-1
        while k[p1] == nums[p1]:
            p1 += 1
        while k[p2] == nums[p2]:
            p2 -= 1
        return p2-p1+1

num = [2,6,4,8,10,9,15]
print(Solution().findUnsortedSubarray(num))