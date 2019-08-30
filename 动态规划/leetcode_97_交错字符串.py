class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1,n1 + 1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
            else:
                dp[i][0] = False
        for i in range(1,n2 + 1):
            if s2[:i] == s3[:i]:
                dp[0][i] = True
            else:
                dp[0][i] = False

        for i in range(1,n1 + 1):
            for j in range(1,n2 + 1):
                dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1])
        return dp[-1][-1]

