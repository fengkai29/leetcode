class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = 0
        count = 1
        a = 0
        s = ""
        if len(strs) == 1:
            return strs[0]
        if strs == []:
            return s
        else:
            for m in range(len(strs)):
                if len(strs[m])>length:
                    length = len(strs[m])
            for i in range(length+1):
                a = i
                if count:
                    for j in range(len(strs)-1):
                        if strs[j][:i] != strs[j+1][:i]:
                            a = a - 1
                            count = 0
                            break

                if count == 0:
                    break
            if a == -1:
                return s
            s = s+strs[0][:a]
            return s

a = ["a","a"]
t = Solution().longestCommonPrefix(a)
print('"%s"'%t)