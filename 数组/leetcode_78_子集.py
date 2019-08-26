class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        ans.append([])
        self.back(nums,ans)
        return ans
    def back(self,temp,ans,res = []):
        for j in range(len(temp)):
           ans.append(res+[temp[j]])
           self.back(temp[j+1:],ans,res+[temp[j]])



m = [1,2,3]
t = Solution().subsets(m)
print(t)