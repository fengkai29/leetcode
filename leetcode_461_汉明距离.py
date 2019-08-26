class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = []
        b = []
        count = 0
        while x != 0:
            a.append(x%2)
            x = int(x/2)
        while y != 0:
            b.append(y%2)
            y = int(y/2)
        if len(a)> len(b):
            for i in range(len(b)):
               if a[i] != b[i]:
                   count = count + 1
            return (count + a[len(b):len(a)].count(1))
        else:
            for i in range(len(a)):
               if a[i] != b[i]:
                   count = count + 1
            return (count + b[len(a):len(b)].count(1))

s = 1
k = 4
print(Solution().hammingDistance(s,k))