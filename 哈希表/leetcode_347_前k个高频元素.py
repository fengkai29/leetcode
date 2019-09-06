class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        seq = list(set(nums))
        dic = dict.fromkeys(seq,0)
        for i in nums:
            dic[i] = dic[i] + 1
        print(dic)
        dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for i in range(k):
            out.append(dic[i][0])
        return out


a = [4,1,-1,2,-1,2,3]
k = 2
print(Solution().topKFrequent(a,k))
