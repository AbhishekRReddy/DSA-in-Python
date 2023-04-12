'''
https://www.codingninjas.com/codestudio/problems/maximum-path-sum-in-the-matrix_797998?leftPanelTab=0
'''
'''
DP with Memoization
'''

def maxip(m,n,matrix,dp):
    if n < 0 or n >= len(matrix[0]):
        return float('-inf')
    if m == 0:
        return matrix[m][n]
    if dp[m][n] != -1:
        return dp[m][n]
    up = matrix[m][n] + maxip(m-1,n,matrix,dp)
    left = matrix[m][n] + maxip(m-1,n-1,matrix,dp)
    right = matrix[m][n] + maxip(m-1,n+1,matrix,dp)
    dp[m][n] = max(up, max(left,right))
    return dp[m][n]


def getMaxPathSum(matrix):
    #   Write your code here
    m = len(matrix)
    n = len(matrix[0])
    global_maxi = float('-inf')
    dp = [[-1]*n for i in range(m)]
    for col in range(n):
        global_maxi = max(global_maxi,maxip(m-1,col,matrix,dp))
    return global_maxi
