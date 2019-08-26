class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        a = []
        if len(s)==0:
            return True
        else:
            for i in range(len(s)):
               if len(a)==0 and (s[i] == ')' or s[i] == ']' or s[i] == '}'):
                   return False
               if s[i] == '(' or s[i] == '[' or s[i] == '{':
                   a.append(s[i])
               elif s[i] == ')' and a[len(a)-1] == '(':
                   del a[len(a)-1]
               elif s[i] == ']' and a[len(a)-1] == '[':
                   del a[len(a) - 1]
               elif s[i] == '}' and a[len(a)-1] == '{':
                   del a[len(a)-1]
               else:
                   return False
            if len(a)==0:
                return True
            else:
                return False


s = "(])"
t =Solution().isValid(s)
print(t)