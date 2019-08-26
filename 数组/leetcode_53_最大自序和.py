class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1] and nums[i-1]>0:
                nums[i]=nums[i]+nums[i-1]
            elif nums[i]>=nums[i-1] and nums[i-1]>0:
                nums[i]=nums[i]+nums[i-1]
        return max(nums)





n = [1,2,-1,-2,2,1,-2,1,4,-5,4]
t = Solution().maxSubArray(n)
print(t)