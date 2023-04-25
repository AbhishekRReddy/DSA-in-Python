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

'''
DP with Memoization
'''
def f(ind,buy,prices,dp):
    if ind == len(prices):
        return 0
    profit = 0
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    if buy == 1:
        pur = -prices[ind] + f(ind+1,0,prices,dp)
        not_pur = f(ind+1, 1, prices,dp)
        profit = max(pur,not_pur) 
    else:
        sell = prices[ind] + f(ind+1, 1, prices,dp)
        not_sell = f(ind+1,0,prices,dp)
        profit = max(sell,not_sell)
    dp[ind][buy] = profit
    return dp[ind][buy]
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [ [-1,-1] for _ in range(len(prices)+1)]
        return f(0,1,prices,dp)

