class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = []
        count = 0
        while num > 0:
            a.append(num%2)
            num = int(num/2)
        for i in range(len(a)):
            if a[i] == 0:
                count = count + pow(2,i)
        return count
