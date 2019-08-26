class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < (len(nums)-nums.count(0)):
            if nums[i] == 0:
                del nums[i]
                nums.append(nums[i])
            else:
                i += 1