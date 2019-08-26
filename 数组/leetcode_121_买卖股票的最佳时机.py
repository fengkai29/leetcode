class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if count< prices[j]-prices[i]:
        #             count = prices[j]-prices[i]
        # return count
        if prices == []:
            return 0
        else:
            count = 0
            min_flag = prices[0]
            for i in prices:
                count = max(count,i-min_flag)
                min_flag = min(min_flag,i)
            return count