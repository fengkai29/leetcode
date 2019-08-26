class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if i == len(nums)-1:
                if count > flag:
                    flag = count
            if nums[i] == 0:
                if count > flag:
                    flag = count
                count = 0
        return flag
a = [1,1]
print(Solution().findMaxConsecutiveOnes(a))