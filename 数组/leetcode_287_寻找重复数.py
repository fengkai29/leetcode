class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        nums = sorted(nums)
        while nums.count(int((start+end)/2))<=1 and start<end:
            if nums[int((start+end)/2)]<int((start+end)/2):
                end = int((start+end)/2)-1
            else:
                start = int((start+end)/2)+1
        return int((start+end)/2)

m = [1,3,4,2,1]
print(Solution().findDuplicate(m))