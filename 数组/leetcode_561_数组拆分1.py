class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(0,len(nums)-1,2):
            count = count+nums[i]
        return count

count1 = [1,4,3,2]
print(Solution().arrayPairSum(count1))