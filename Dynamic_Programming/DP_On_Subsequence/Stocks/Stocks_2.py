'''
This is DP apprpach rather than Greedy
'''
def f(ind,buy,prices):
    if ind == len(prices):
        return 0
    profit = 0
    if buy:
        buy = -prices[ind] + f(ind+1,False,prices)
        not_buy = f(ind+1, True, prices)
        profit = max(buy,not_buy) 
    else:
        sell = prices[ind] + f(ind+1, True, prices)
        not_sell = f(ind+1, False,prices)
        profit = max(sell,not_sell)
    return profit

class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        return f(0,True,prices)
