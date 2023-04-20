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
    
'''
DP with Tabulation method
'''

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n+1):
            left = dp[i-1]
            right = dp[i-2]
            if i < n:
                left += cost[i]
                right += cost[i]
            dp[i] = min(left,right)
        return dp[n]

'''
DP tabulation with space optimization
'''
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev1 = cost[1]
        curr = 0
        for i in range(2,n+1):
            left = prev1
            right = prev2
            if i < n:
                left += cost[i]
                right += cost[i]
            curr = min(left,right)
            prev2 = prev1
            prev1 = curr
        return curr