class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        count = 1
        m = len(candies)/2
        candies.sort()
        for i in range(1,len(candies)):
            if candies[i] != candies[i-1]:
                count += 1
        if count > m :
            return m
        else:
            return count

a = [1,1,1,1,2,2,2,3,3,3]

print(Solution().distributeCandies(a))