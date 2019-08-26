class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        a = []
        b = []
        while len(piles)>2:
            if piles[len(piles)-2]-piles[len(piles)-1]>=piles[1]-piles[0]:
                a.append(piles[0])
                del piles[0]
            else:
                a.append(piles[len(piles)-1])
                del piles[len(piles)-1]
            if piles[len(piles)-2]-piles[len(piles)-1]>=piles[1]-piles[0]:
                a.append(piles[0])
                del piles[0]
            else:
                a.append(piles[len(piles)-1])
                del piles[len(piles)-1]
        a.append(max(piles))
        b.append(min(piles))
        if sum(a)>sum(b):
            return True
        else:
            return False