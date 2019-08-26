class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = 0
        # pre = 0
        # cur = 0
        # for i in range(len(nums)):
        #     temp = cur
        #     cur = max(pre+nums[i], cur)
        #     pre = temp
        # return cur
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i in range(2,len(nums)):
            a =nums[:i-1]
            nums[i] = max(a)+nums[i]
        return max(nums)