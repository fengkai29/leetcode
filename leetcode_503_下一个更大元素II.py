class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in  range(len(nums)):
            flag = 0
            flag1 = 0
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    res.append(nums[j])
                    flag = 1
                    break
            if flag == 0:
                for j in range(0,i):
                    if nums[j]>nums[i]:
                        res.append(nums[j])
                        flag1 = 1
                        break
            if flag == 0 and flag1 == 0:
                res.append(-1)

        return res
