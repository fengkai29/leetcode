class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort_nums = sorted(nums,reverse=True)
        res = []
        for m in nums:
            if sort_nums.index(m)+1 == 1:
                res.append("Gold Medal")
            elif sort_nums.index(m)+1 == 2:
                res.append("Silver Medal")
            elif sort_nums.index(m)+1 == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(sort_nums.index(m)+1))
        return res

num = [5, 4, 3, 2, 1]
print(Solution().findRelativeRanks(num))