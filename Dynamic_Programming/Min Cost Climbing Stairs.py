'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/
'''
'''
DP with Memoization
'''
def minc(cost, n,dp):
    if n == 0:
        return cost[0]
    if n == 1:
        return cost[1]
    if dp[n] != -1:
        return dp[n]
    left = minc(cost, n-1,dp)
    right = minc(cost,n-2,dp)
    if n < len(cost):
        left += cost[n]
        right += cost[n]
    dp[n] = min(left,right)
    return dp[n]
    
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        return minc(cost,n,dp)