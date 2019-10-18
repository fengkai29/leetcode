class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        ls = [S[0]]
        for i in range(1,len(S)):
            if ls != []:
                if S[i] == ls[-1]:
                    del ls[-1]
                else:
                    ls.append(S[i])
            else:
                ls.append(S[i])
        m = ''
        for i in ls:
            m += i
        return m

S = "abbaca"

print(Solution().removeDuplicates(S))