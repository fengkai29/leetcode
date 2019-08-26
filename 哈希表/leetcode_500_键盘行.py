class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        a2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        a3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        s = []
        for i in range(len(words)):
            if words[i][0] in a1:
                flag = 1
            if words[i][0] in a2:
                flag = 2
            if words[i][0] in a3:
                flag = 3
            for j in range(len(words[i])):
                if flag == 1:
                    if words[i][j] not in a1:
                        break
                if flag == 2:
                    if words[i][j] not in a2:
                        break
                if flag == 3:
                    if words[i][j] not in a3:
                        break
                if j == len(words[i])-1:
                    s.append(words[i])
        return s