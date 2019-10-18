class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            digits[-1] =0
            index = 1
            while index<len(digits):
                if digits[-1-index] != 9:
                    digits[-1-index] = digits[-1-index]+1
                    break
                digits[-1-index] = 0
                index = index + 1
            if index == len(digits):
                digits.insert(0,1)
        else:
            digits[-1] = digits[-1]+1
        return digits