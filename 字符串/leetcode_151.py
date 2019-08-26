class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ''
        b = s.split(' ')
        a = []
        for j in range(len(b)):
            if b[j] != '':
                a.append(b[j])
        for i in range(len(a)):
            if i == len(a)-1:
                m = m + a[len(a)-i-1]
            else:
                m = m + a[len(a)-i-1]+' '

        return m

a = "  hello world!  "
t = Solution().reverseWords(a)
print(t)