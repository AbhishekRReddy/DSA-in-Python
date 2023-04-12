'''
https://leetcode.com/problems/minimum-path-sum/description/
'''

'''
DP with Memoization.
'''
def minips(m,n,grid,dp):
    if m == 0 and n == 0:
        return grid[m][n]
    if m < 0 or n < 0:
        return float('inf')
    if dp[m][n] != -1:
        return dp[m][n]
    up = grid[m][n] + minips(m-1,n,grid,dp)
    left = grid[m][n] + minips(m,n-1,grid,dp)
    dp[m][n] = min(up,left)
    return dp[m][n]

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        return minips(m-1,n-1,grid,dp)