class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        end = []
        for num in arr1:
            if num not in arr2:
                end.append(num)

        end = sorted(end)
        start = []
        for num in arr2:
            k = arr1.count(num)
            for i in range(k):
                start.append(num)
        output = start + end
        return output