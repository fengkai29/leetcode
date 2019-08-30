# class Solution(object):
#     def coinChange(self, coins, amount):
#         """
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
#         if amount == 0:
#             return 0
#         else:
#             u = []
#             u.append(amount)
#             ls = [amount]
#             count = 0
#             while ls != []:
#                 m = []
#                 for tem in ls:
#                     for i in range(len(coins)):
#                         if tem - coins[i] >= 0 and (tem - coins[i]) not in u:
#                             u.append(tem-coins[i])
#                             m.append(tem-coins[i])
#                 if 0 in m:
#                     return count+1
#                 ls = list(set(m[:]))
#                 count = count + 1
#
#             if ls == []:
#                 return -1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [0 for _ in range(amount + 1)]

        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


coins = [431,62,88,428]

amount = 9084
print(Solution().coinChange(coins,amount))