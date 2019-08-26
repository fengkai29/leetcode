class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = s+'I'
        i = 0
        while i<len(s)-1:
            j = i
            if s[i] == 'I' and s[i+1] =='V':
                count = count+4
                j = i + 1
            if s[i] == 'I' and s[i+1] =='X':
                count = count+9
                j = i + 1
            if s[i] == 'I' and s[i+1] !='V' and s[i+1] !='X':
                count = count + 1
            if s[i] == 'X' and s[i+1] =='L':
                count = count+40
                j = i + 1
            if s[i] == 'X' and s[i+1] =='C':
                count = count+90
                j = i + 1
            if s[i] == 'X' and s[i+1] !='L' and s[i+1] !='C':
                count = count + 10
            if s[i] == 'C' and s[i+1] =='D':
                count = count+400
                j = i + 1
            if s[i] == 'C' and s[i+1] =='M':
                count = count+900
                j = i + 1
            if s[i] == 'C' and s[i+1] !='D' and s[i+1] !='M':
                count = count + 100
            if s[i] == 'V':
                count =count+5
            if s[i] == 'L':
                count =count+50
            if s[i] == 'D':
                count =count+500
            if s[i] == 'M':
                count =count+1000
            i = j+1
        return count

str = "MCMXCIV"
m = Solution().romanToInt(str)
print(m)