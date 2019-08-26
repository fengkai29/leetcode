# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         a = ['']
#         b = ['']
#         for i in range(len(t)):
#             for j in a:
#                 m = j+t[i]
#                 if m not in b:
#                     b.append(m)
#             a = b[:]
#         if s in a:
#             return True
#         else:
#             return False

# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s)<1:
#             return False
#         i=0
#         j=0
#         while i<len(t):
#             while j<len(s):
#                 if s[j]==t[i]:
#                     j+=1
#                     i+=1
#                 elif t[i]==s[0]:
#                     j=0
#                 else:
#                     i+=1
#         if j==len(s):
#             return True
#         else:return False

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        j = 0
        for i in range(len(t)):
            if s[j] == t[i]:
                j = j+1
            if j == len(s):
                break
        if j == len(s):
            return True
        else:
            return False



s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s,t))