class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        nums = [i for i in range(len(S)+1)]
        out = []
        # if S[0] == 'I':
        #     out.append(0)
        #     del nums[0]
        # else:
        #     out.append(nums[-1])
        #     del nums[-1]
        for i in range(0,len(S)):
            if S[i] == 'D':
                out.append(nums[-1])
                del nums[-1]
            else:
                out.append(nums[0])
                del nums[0]
        out.append(nums[0])
        return out

