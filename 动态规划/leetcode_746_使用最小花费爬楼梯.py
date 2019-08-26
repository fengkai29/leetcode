class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)==1:
            return 0
        if len(cost)==2:
            return min(cost)
        for i in range(2,len(cost)):
            if cost[i-1]>cost[i-2]:
                cost[i]=cost[i]+cost[i-2]
            else:
                cost[i]=cost[i]+cost[i-1]
        return min(cost[len(cost)-1],cost[len(cost)-2])