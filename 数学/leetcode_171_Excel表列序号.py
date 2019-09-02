class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s),0,-1):
            result = result + (ord(s[len(s)-i])-64)*pow(26,i-1)
        return result

print(Solution().titleToNumber('AZ'))
