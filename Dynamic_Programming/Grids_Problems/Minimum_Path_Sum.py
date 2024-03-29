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

'''
DP with Tabulation
'''
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                up = float('inf')
                left = float('inf')
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                dp[i][j] = min(up,left)
        return dp[m-1][n-1]

'''
DP with Tabulation with Space Optimization
'''