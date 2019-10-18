class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return
        ls = []
        for i in range(len(nums)-k+1):
            ls.append(max(nums[i:i+k]))
        return ls