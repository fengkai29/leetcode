class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        s = ''
        t = address.split('.')
        for j in range(3):
            s = s + t[j] + '[.]'
        s = s + t[3]
        return s
