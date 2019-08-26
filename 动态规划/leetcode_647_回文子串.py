class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                t = s[i:j]
                if s[i:j]==t[::-1]:
                    count = count + 1
        return count