class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            del nums1[m+n-1-i]
        for j in range(n):
            nums1.append(nums2[j])
        nums1.sort()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
t = Solution().merge(nums1,m,nums2,n)
print(nums1)

