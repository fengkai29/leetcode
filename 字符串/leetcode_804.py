class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a = []
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(len(words)):
            s = ''
            for j in range(len(words[i])):
                s = s+m[ord(words[i][j])-97]
            if s not in a:
                a.append(s)

        return len(a)


c = ["gin", "zen", "gig", "msg"]
t = Solution().uniqueMorseRepresentations(c)
print(t)

