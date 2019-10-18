class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        index = []
        for i in range(len(S)):
            if S[i] == C:
                index.append(i)
        dp = [0] * len(S)
        for i in range(len(S)):
            dp[i] = min([abs(j-i) for j in index])
        return dp