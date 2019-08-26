class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count  = 0
        for i in range(len(J)):
            m = J[i]
            for j in range(len(S)):
                if m == S[j]:
                    count = count + 1
        return count

# return sum(S.count(i) for i in J)