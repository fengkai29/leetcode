class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

m = [10,9,2,5,3,4]
print(Solution().lengthOfLIS(m))