class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        a = heights[:]
        heights.sort()
        for i in range(len(heights)):
            if a[i] != heights[i]:
                count = count + 1
        return count
