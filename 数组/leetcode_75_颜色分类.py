class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(len(nums)):
            if nums[0] == 0:
                count1 = count1 + 1
            if nums[0] == 1:
                count2 = count2 + 1
            if nums[0] == 2:
                count3 = count3 + 1
            del nums[0]
        for i in range(count1):
            nums.append(0)
        for i in range(count2):
            nums.append(1)
        for i in range(count3):
            nums.append(2)

a = [0]
Solution().sortColors(a)
