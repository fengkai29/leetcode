class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = ''
        ls = list(s.split(' '))
        for i in range(len(ls)-1):
            ls[i] = ls[i][::-1]
            k = k + ls[i] + ' '
        k = k + ls[-1][::-1]
        return k
m = "Let's take LeetCode contest"
print(Solution().reverseWords(m))