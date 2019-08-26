class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # flag = [1,0]
        # if len(nums) == 0:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(2,len(nums)-1):
        #     a =nums[:i-1]
        #     nums[i] = max(a)+nums[i]
        #     if flag[nums.index(max(a))] == 1:
        #         flag.append(1)
        #     else:
        #         flag.append(0)
        # if len(nums)>2:
        #     b = nums[:len(nums)-2]
        #     if flag[nums.index(max(b))] == 1:
        #         nums[len(nums)-1] = max(b)+nums[len(nums)-1]-nums[0]
        #     if flag[nums.index(max(b))] == 0:
        #         nums[len(nums)-1] = max(b)+nums[len(nums)-1]
        # return max(nums)
        m = []
        n = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2 or len(nums)==3:
            return max(nums)
        m.append(nums[0])
        m.append(nums[1])
        n.append(nums[0])
        n.append(nums[1])
        n.append(nums[2])
        for i in range(2,len(nums)-1):
            a =m[:i-1]
            m.append(max(a)+nums[i])
        for j in range(3,len(nums)):
            b = n[1:j-1]
            n.append(max(b)+nums[j])
        return max(max(m),max(n))


a = [4,1,2,7,5,3,1]
print(Solution().rob(a))
