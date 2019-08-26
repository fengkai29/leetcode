class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        nums = list(nums)
        del nums[nums.index(max(nums))]
        del nums[nums.index(max(nums))]
        return max(nums)