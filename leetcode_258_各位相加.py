class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            self.vice(num)
            num = self.vice(num)
        return num

    def vice(self,num):
        a = []
        while num > 0:
            a.append(num % 10)
            num = int(num / 10)
        return sum(a)