class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        num = [0]*num_people
        flag = 1
        tem = 0
        while True:
            for i in range(num_people):
                if flag + sum(num) >= candies:
                    count = i
                    tem = 1
                    break
                num[i] = num[i] + flag
                flag = flag + 1
            if tem:
                break
        num[i] = candies-sum(num)+num[i]
        return num

