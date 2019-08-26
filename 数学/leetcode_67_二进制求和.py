class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = []
        m = ''
        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(len(a)):
            count1 = count1 + int(a[i])*pow(2,len(a)-1-i)
        for j in range(len(b)):
            count2 = count2 + int(b[j])*pow(2,len(b)-1-j)
        count3 = count1 + count2
        if count3 == 0:
            return '0'
        while count3:
            s.append(count3%2)
            count3 = count3 / 2
        for k in range(len(s)):
            m = m+str(s[len(s)-k-1])
        return m