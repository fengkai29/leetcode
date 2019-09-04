class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        ls = []
        for i in range(0,len(s),k):
            ls.append(s[i:i+k])
        for i in range(0,len(ls),2):
            ls[i] = ls[i][::-1]
        for i in range(len(ls)):
            result = result + ls[i]
        return result


print(Solution().reverseStr('abcdefg',2))