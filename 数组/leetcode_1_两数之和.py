class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i in range(len(nums)):
            m = target - nums[i]
            v = nums[i]
            del nums[i]
            if m in nums:
                a.append(i)
                a.append(nums.index(m)+1)
                return a
            nums.insert(i,v)

nums = [1,2,1,4]
target = 2
t = Solution()
m = t.twoSum(nums,target)
print(m)