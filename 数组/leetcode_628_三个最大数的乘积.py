class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        a = max(nums)
        del nums[nums.index(max(nums))]
        b = max(nums)
        del nums[nums.index(max(nums))]
        c = max(nums)
        d = min(nums)
        del nums[nums.index(min(nums))]
        f = min(nums)
        if a * b * c > a * d * f:
            return a * b * c
        else:
            return a * d * f
