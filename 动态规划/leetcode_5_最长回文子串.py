class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s
        for i in range(len(s),0,-1):
            for j in range(len(s)):
                if j+i>len(s):
                    break
                temp = s[j:j+i]
                if temp == temp[::-1]:
                    return temp

s = "1234224"
print(Solution().longestPalindrome(s))
