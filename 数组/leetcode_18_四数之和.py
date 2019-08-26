class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)<4:
            return res
        elif len(nums)==4:
            if nums[0]+nums[1]+nums[2]+nums[3] == target:
                res.append(nums)
                return res
        else:
            temp = [0,0,0,0]
            for i in range(len(nums)-3):
                temp[0] = nums[i]
                for j in range(i+1,len(nums)):
                    temp[1] = nums[j]
                    for k in range(j+1,len(nums)):
                        temp[2] = nums[k]
                        for l in range(k+1,len(nums)):
                            temp[3] = nums[l]
                            if temp[0]+temp[1]+temp[2]+temp[3] == target:
                                b = temp[:]
                                b.sort()
                                if b not in res:
                                    res.append(b)
            return res

nums = [0,0,1,0,0]
target = 1
t = Solution().fourSum(nums,target)
print(t)