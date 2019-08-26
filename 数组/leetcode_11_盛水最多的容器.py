class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        count = 0
        while i<j:
            if height[i]<height[j]:
                count = max(count,(j-i)*height[i])
                i += 1
            else:
                count = max(count,(j-i)*height[j])
                j -= 1
        return count