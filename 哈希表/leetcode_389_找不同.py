class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = int(ord(s[0]))
        for i in range(1,len(s)):
            res = res ^ int(ord(s[i]))
        for i in range(len(t)):
            res = res ^ int(ord(t[i]))
        return chr(res)

s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s,t))