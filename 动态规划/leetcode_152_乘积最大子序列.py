class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpmax = [0] * len(nums)
        dpmin = [0] * len(nums)
        dpmax[0] = dpmin[0] = nums[0]
        for i in range(1,len(nums)):
            a1 = dpmax[i-1]*nums[i]
            a2 = dpmin[i-1]*nums[i]
            a3 = nums[i]
            dpmax[i] = max(a1,a2,a3)
            dpmin[i] = min(a1,a2,a3)
        return max(dpmax)
