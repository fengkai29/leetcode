# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """
#         flag = 0
#         s1 = []
#         for i in wordDict:
#             if len(i) <= len(s):
#                 j = 0
#                 while j < len(i):
#                     if i[j] != s[j]:
#                         break
#                     j = j+1
#                 if j == len(i):
#                     s1.append(s[len(i):])
#                 if j == len(i) and len(s) == len(i):
#                     flag = 1
#         s = list(s)
#
#         while True:
#             if s1 == s and flag == 0:
#                 return False
#             if flag == 1:
#                 return True
#             s = s1[:]
#             s1 = []
#             for word in wordDict:
#                 for c_word in s:
#                     if len(word) <= len(c_word):
#                         j = 0
#                         while j < len(word):
#                             if word[j] != c_word[j]:
#                                 break
#                             j = j + 1
#                         if j == len(word):
#                             s1.append(c_word[len(word):])
#                         if j == len(word) and len(word) == len(c_word):
#                             flag = 1
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if not wordDict: return not s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


s = "applepenapple"
word = ["apple","pen"]
print(Solution().wordBreak(s,word))