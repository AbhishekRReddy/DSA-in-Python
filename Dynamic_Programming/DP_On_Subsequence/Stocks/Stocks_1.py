'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            local_profit = prices[i] - mini
            profit = max(profit, local_profit)
            mini = min(mini, prices[i])
        return profit