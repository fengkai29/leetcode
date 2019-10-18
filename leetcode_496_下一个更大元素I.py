class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for elem in nums1:
            flag = 1
            for i in range(nums2.index(elem)+1,len(nums2)):
                if nums2[i]>elem:
                    res.append(nums2[i])
                    flag = 0
                    break
            if flag:
                res.append(-1)
        return res

