# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count = 0
#         for i in range(len(nums)):
#             flag = nums[i]
#             for j in range(i+1,len(nums)+1):
#                 if flag == k:
#                     count = count + 1
#                 if j <= len(nums)-1:
#                     flag = flag + nums[j]
#
#         return count

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum, res, cul = 0, 0, {}
        cul[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in cul:
                res += cul[sum - k]
            if sum not in cul:
                cul[sum] = 0
            cul[sum] += 1
        return res

nums = [1,1,1]

k = 2
print(Solution().subarraySum(nums,k))