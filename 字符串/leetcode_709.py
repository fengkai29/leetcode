class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ''
        str = list(str)
        for i in range(len(str)):
            if str[i]>='A' and str[i]<='Z':
                a = chr(ord(str[i])+32)
            else:
                a = str[i]
            s = s + a
        return s

st = 'SDFSF'
t = Solution().toLowerCase(st)
print(t)